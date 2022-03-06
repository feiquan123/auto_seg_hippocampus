import os
import joblib
from glob import glob
import torch
from tqdm import tqdm
import imageio
from skimage.io import imread, imsave
# from hausdorff import hausdorff_distance
import numpy as np
import warnings

import deepresunet_brats.mymodel as mymodel
from deepresunet_brats.dataset import Dataset
from deepresunet_brats.metrics import dice_coef,  ppv,sensitivity
from data_pre import IMAGE_PATH,MASK_PATH,output_data_test_root
from error_code import (
	SUCCESS,
	ERROR_IMAGE_TEST_DATA_PATH_NOT_EXISTS,ERROR_MASK_TEST_DATA_PATH_NOT_EXISTS,
	ERROR_UNKNOWN_ARCH,
	ERROR_OUTPUT_GT_TEST_DATA_EMPTY,ERROR_OUTPUT_TEST_DATA_EMPTY
)

Models_PATH = os.path.join(
	os.path.dirname(os.path.abspath(__file__)),"models"
)
Model_Name = "hublock1_DeepResUNet_woDS"
Model_Calculate_Mode = "Calculate"
Model_GetPicture_Mode = "GetPicture"

Arch_DeepResUNet = "DeepResUNet"
Arch_HybridResUNet = "HybridResUNet"
Arch_ONet = "ONet"
Archs = {
	Arch_DeepResUNet:Arch_DeepResUNet,
	Arch_HybridResUNet:Arch_HybridResUNet,
	Arch_ONet:Arch_ONet,
}

def data_test(dataPreOutPutPath:str, isCUDA=True, mode=Model_GetPicture_Mode,arch="")->dict:
	image_path = os.path.join(dataPreOutPutPath,IMAGE_PATH)
	mask_path = os.path.join(dataPreOutPutPath,MASK_PATH)
	if not os.path.exists(image_path):
		return ERROR_IMAGE_TEST_DATA_PATH_NOT_EXISTS.__dict__()
	if not os.path.exists(mask_path):
		return ERROR_MASK_TEST_DATA_PATH_NOT_EXISTS.__dict__()

	# 加载参数
	pkl_path = os.path.join(Models_PATH,Model_Name,"args.pkl")
	args = joblib.load(pkl_path)
	if len(arch) > 0:
		args.arch = arch
	if Archs.get(args.arch,None) is None:
		return ERROR_UNKNOWN_ARCH.__dict__()

	print('----- config args -----')
	for arg in vars(args):
		print('%s:\t%s' %(arg, getattr(args, arg)))
	print('-----------------------')

	# 指定输出文件是否存在
	basename = os.path.dirname(dataPreOutPutPath)
	output_path = os.path.join(basename,output_data_test_root,args.arch)
	if not os.path.exists(output_path):
		os.makedirs(output_path)
	elif mode == Model_GetPicture_Mode:
		# 如果已经测试过就不需要再次测试
		return SUCCESS.with_data({
			"dataTestOutputPath": output_path,
		})

	# create model
	model = mymodel.__dict__[args.arch](args)
	pth_path= os.path.join(Models_PATH,Model_Name,"model.pth")
	if isCUDA:
		model = model.cuda()
		model.load_state_dict(torch.load(pth_path))
	else:
		model.load_state_dict(torch.load(pth_path, map_location=torch.device('cpu')))
	model.eval()

	val_img_paths = glob(os.path.join(image_path,'*'))
	val_mask_paths = glob(os.path.join(mask_path,'*'))
	val_dataset = Dataset(args, val_img_paths,val_mask_paths)
	val_loader = torch.utils.data.DataLoader(
		val_dataset,
		batch_size=args.batch_size,
		shuffle=False,
		pin_memory=True,
		drop_last=False)

	if mode == Model_GetPicture_Mode:
		get_picture_mode(
			model=model,
			args=args,
			val_loader = val_loader,
			val_img_paths = val_img_paths,
			val_mask_paths = val_mask_paths,
			output_path = output_path,
			isCUDA = isCUDA,
		)

	if mode == Model_Calculate_Mode:
		maskPath = glob(os.path.join(output_path,"GT","*.png"))
		pbPath = glob(os.path.join(output_path,"*.png"))
		if len(maskPath) == 0:
			return ERROR_OUTPUT_GT_TEST_DATA_EMPTY.__dict__()
		if len(pbPath) == 0:
			return ERROR_OUTPUT_TEST_DATA_EMPTY.__dict__()

		calculate_mode(
			maskPath= maskPath,
			pbPath = pbPath,
		)

	re = SUCCESS.with_data({
		"dataTestOutputPath": output_path,
	})
	return re

def get_picture_mode(model,args,val_loader,val_img_paths,val_mask_paths,output_path, isCUDA=True):
	with warnings.catch_warnings():
		warnings.simplefilter('ignore')

		with torch.no_grad():
			for i, (input, target) in tqdm(enumerate(val_loader), total=len(val_loader)):
				if isCUDA:
					input = input.cuda()
				#target = target.cuda()

				# compute output
				if args.deepsupervision:
					output = model(input)[-1]
				else:
					output = model(input)
				#print("img_paths[i]:%s" % img_paths[i])
				output = torch.sigmoid(output).data.cpu().numpy()
				img_paths = val_img_paths[args.batch_size*i:args.batch_size*(i+1)]
				#print("output_shape:%s"%str(output.shape))


				for i in range(output.shape[0]):
					npName = os.path.basename(img_paths[i])
					overNum = npName.find(".npy")
					rgbName = npName[0:overNum]
					rgbName = rgbName  + ".png"
					rgbPic = np.zeros([160, 160, 3], dtype=np.uint8)
					for idx in range(output.shape[2]):
						for idy in range(output.shape[3]):
							if output[i,0,idx,idy] > 0.5:
								rgbPic[idx, idy, 0] = 0
								rgbPic[idx, idy, 1] = 128
								rgbPic[idx, idy, 2] = 0
							if output[i,1,idx,idy] > 0.5:
								rgbPic[idx, idy, 0] = 255
								rgbPic[idx, idy, 1] = 0
								rgbPic[idx, idy, 2] = 0
							if output[i,2,idx,idy] > 0.5:
								rgbPic[idx, idy, 0] = 255
								rgbPic[idx, idy, 1] = 255
								rgbPic[idx, idy, 2] = 0
					imsave(os.path.join(output_path, rgbName),rgbPic)

		torch.cuda.empty_cache()
	
	print("Saving GT,numpy to picture")
	val_gt_path = os.path.join(output_path, "GT")
	if not os.path.exists(val_gt_path):
		os.mkdir(val_gt_path)
	for idx in tqdm(range(len(val_mask_paths))):
		mask_path = val_mask_paths[idx]
		name = os.path.basename(mask_path)
		overNum = name.find(".npy")
		name = name[0:overNum]
		rgbName = name + ".png"

		npmask = np.load(mask_path)

		GtColor = np.zeros([npmask.shape[0],npmask.shape[1],3], dtype=np.uint8)
		for idx in range(npmask.shape[0]):
			for idy in range(npmask.shape[1]):
				
				if npmask[idx, idy] == 1:
					GtColor[idx, idy, 0] = 255
					GtColor[idx, idy, 1] = 0
					GtColor[idx, idy, 2] = 0
				
				elif npmask[idx, idy] == 2:
					GtColor[idx, idy, 0] = 0
					GtColor[idx, idy, 1] = 128
					GtColor[idx, idy, 2] = 0
				
				elif npmask[idx, idy] == 4:
					GtColor[idx, idy, 0] = 255
					GtColor[idx, idy, 1] = 255
					GtColor[idx, idy, 2] = 0

		imageio.imwrite(os.path.join(val_gt_path,rgbName), GtColor)
	print("Done!")


def calculate_mode( maskPath , pbPath:list):
	wt_dices = []
	tc_dices = []
	et_dices = []
	wt_sensitivities = []
	tc_sensitivities = []
	et_sensitivities = []
	wt_ppvs = []
	tc_ppvs = []
	et_ppvs = []
	wt_Hausdorf = []
	tc_Hausdorf = []
	et_Hausdorf = []

	wtMaskList = []
	tcMaskList = []
	etMaskList = []
	wtPbList = []
	tcPbList = []
	etPbList = []

	for myi in tqdm(range(len(maskPath))):
		mask = imread(maskPath[myi])
		pb = imread(pbPath[myi])

		wtmaskregion = np.zeros([mask.shape[0], mask.shape[1]], dtype=np.float32)
		wtpbregion = np.zeros([mask.shape[0], mask.shape[1]], dtype=np.float32)

		tcmaskregion = np.zeros([mask.shape[0], mask.shape[1]], dtype=np.float32)
		tcpbregion = np.zeros([mask.shape[0], mask.shape[1]], dtype=np.float32)

		etmaskregion = np.zeros([mask.shape[0], mask.shape[1]], dtype=np.float32)
		etpbregion = np.zeros([mask.shape[0], mask.shape[1]], dtype=np.float32)

		for idx in range(mask.shape[0]):
			for idy in range(mask.shape[1]):
				
				if mask[idx, idy, :].any() != 0:
					wtmaskregion[idx, idy] = 1
				if pb[idx, idy, :].any() != 0:
					wtpbregion[idx, idy] = 1
				
				if mask[idx, idy, 0] == 255:
					tcmaskregion[idx, idy] = 1
				if pb[idx, idy, 0] == 255:
					tcpbregion[idx, idy] = 1
				
				if mask[idx, idy, 1] == 128:
					etmaskregion[idx, idy] = 1
				if pb[idx, idy, 1] == 128:
					etpbregion[idx, idy] = 1
		
		dice = dice_coef(wtpbregion,wtmaskregion)
		wt_dices.append(dice)
		ppv_n = ppv(wtpbregion, wtmaskregion)
		wt_ppvs.append(ppv_n)
		Hausdorff = hausdorff_distance(wtmaskregion, wtpbregion)
		wt_Hausdorf.append(Hausdorff)
		sensitivity_n = sensitivity(wtpbregion, wtmaskregion)
		wt_sensitivities.append(sensitivity_n)
		
		dice = dice_coef(tcpbregion, tcmaskregion)
		tc_dices.append(dice)
		ppv_n = ppv(tcpbregion, tcmaskregion)
		tc_ppvs.append(ppv_n)
		Hausdorff = hausdorff_distance(tcmaskregion, tcpbregion)
		tc_Hausdorf.append(Hausdorff)
		sensitivity_n = sensitivity(tcpbregion, tcmaskregion)
		tc_sensitivities.append(sensitivity_n)
		
		dice = dice_coef(etpbregion, etmaskregion)
		et_dices.append(dice)
		ppv_n = ppv(etpbregion, etmaskregion)
		et_ppvs.append(ppv_n)
		Hausdorff = hausdorff_distance(etmaskregion, etpbregion)
		et_Hausdorf.append(Hausdorff)
		sensitivity_n = sensitivity(etpbregion, etmaskregion)
		et_sensitivities.append(sensitivity_n)

	print('WT Dice: %.4f' % np.mean(wt_dices))
	print('TC Dice: %.4f' % np.mean(tc_dices))
	print('ET Dice: %.4f' % np.mean(et_dices))
	print("=============")
	print('WT PPV: %.4f' % np.mean(wt_ppvs))
	print('TC PPV: %.4f' % np.mean(tc_ppvs))
	print('ET PPV: %.4f' % np.mean(et_ppvs))
	print("=============")
	print('WT sensitivity: %.4f' % np.mean(wt_sensitivities))
	print('TC sensitivity: %.4f' % np.mean(tc_sensitivities))
	print('ET sensitivity: %.4f' % np.mean(et_sensitivities))
	print("=============")
	print('WT Hausdorff: %.4f' % np.mean(wt_Hausdorf))
	print('TC Hausdorff: %.4f' % np.mean(tc_Hausdorf))
	print('ET Hausdorff: %.4f' % np.mean(et_Hausdorf))
	print("=============")


if __name__ == '__main__':
	dataPreOutPutPath = '/Users/zhi/Program/HTMLProgram/github.com/feiquan123/auto_seg_hippocampus/service/testdata/npy'
	# print(data_test(dataPreOutPutPath,isCUDA=False,mode=Model_GetPicture_Mode,arch=Arch_DeepResUNet))
	print(data_test(dataPreOutPutPath,isCUDA=False,mode=Model_Calculate_Mode,arch=Arch_DeepResUNet))