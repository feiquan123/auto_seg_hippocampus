import os
import shutil

import SimpleITK as sitk
import numpy as np

from error_code import (
	SUCCESS, 
	ERROR_DATA_PATH_NOT_EXISTS,
	ERROR_HGG_DATA_PATH_NOT_EXISTS,ERROR_LGG_DATA_PATH_NOT_EXISTS,
	ERROR_HGG_DATA_EMPTY,ERROR_LGG_DATA_EMPTY,
	ERROR_HGG_DATA_ARRIVE_MAX,ERROR_LGG_DATA_ARRIVE_MAX)

HGG_PATH = "HGG"
LGG_PATH = "LGG"
IMAGE_PATH = "image"
MASK_PATH = "mask"

output_data_pre_root = "npy"
output_data_test_root = "output"

flair_name = "_flair.nii.gz"
t1_name = "_t1.nii.gz"
t1ce_name = "_t1ce.nii.gz"
t2_name = "_t2.nii.gz"
mask_name = "_seg.nii.gz"

def data_pre(dataPrePath:str)->dict:
	# 检测本次预处理的数据是否准备好
	if not os.path.exists(dataPrePath):
		return ERROR_DATA_PATH_NOT_EXISTS.__dict__()
	hgg_path = os.path.join(dataPrePath,HGG_PATH)
	if not os.path.exists(hgg_path):
		return ERROR_HGG_DATA_PATH_NOT_EXISTS.__dict__()	
	lgg_path = os.path.join(dataPrePath,LGG_PATH)	
	if not os.path.exists(lgg_path):
		return ERROR_LGG_DATA_PATH_NOT_EXISTS.__dict__()
	
	# 获取子文件夹下的数据
	hgg_path_list = []
	lgg_path_list = []
	for _,dirs,_ in os.walk(hgg_path):
		hgg_path_list = [os.path.join(hgg_path,x) for x in dirs]
		break
	for _,dirs,_ in os.walk(lgg_path):
		lgg_path_list = [os.path.join(lgg_path,x) for x in dirs]
		break
	if len(hgg_path_list) == 0:
		return ERROR_HGG_DATA_EMPTY.__dict__()
	if len(lgg_path_list) == 0:
		return ERROR_LGG_DATA_EMPTY.__dict__()
	if len(hgg_path_list) > 5:
		return ERROR_HGG_DATA_ARRIVE_MAX.__dict__()
	if len(lgg_path_list) > 5:
		return ERROR_LGG_DATA_ARRIVE_MAX.__dict__()

	# 清空上次预处理后的数据
	output = os.path.join(dataPrePath,output_data_pre_root)
	if os.path.exists(output):
		shutil.rmtree(output,ignore_errors=True)
	# 清空上次测试的数据
	output_test = os.path.join(dataPrePath,output_data_test_root)
	if os.path.exists(output_test):
		shutil.rmtree(output_test,ignore_errors=True)

	# 创建本次预处理需要输出的文件路径
	output_image_path = os.path.join(output,IMAGE_PATH)
	output_mask_path = os.path.join(output,MASK_PATH)
	if not os.path.exists(output_image_path):
		os.makedirs(output_image_path)
	if not os.path.exists(output_mask_path):
		os.makedirs(output_mask_path)

	# 生成 npy 文件
	gen_hgg_npy(hgg_path_list,output_image_path,output_mask_path)
	gen_hgg_npy(lgg_path_list,output_image_path,output_mask_path)

	return SUCCESS.with_data({
		'dataPreOutPutPath': output,
	})

def normalize(slice, bottom=99, down=1):
	"""
	normalize image with mean and std for regionnonzero,and clip the value into range
	:param slice:
	:param bottom:
	:param down:
	:return:
	"""
	#有点像“去掉最低分去掉最高分”的意思,使得数据集更加“公平”
	b = np.percentile(slice, bottom)
	t = np.percentile(slice, down)
	slice = np.clip(slice, t, b)#限定范围numpy.clip(a, a_min, a_max, out=None)

	#除了黑色背景外的区域要进行标准化
	image_nonzero = slice[np.nonzero(slice)]
	if np.std(slice) == 0 or np.std(image_nonzero) == 0:
		return slice
	else:
		tmp = (slice - np.mean(image_nonzero)) / np.std(image_nonzero)
		# since the range of intensities is between 0 and 5000 ,
		# the min in the normalized slice corresponds to 0 intensity in unnormalized slice
		# the min is replaced with -9 just to keep track of 0 intensities
		# so that we can discard those intensities afterwards when sampling random patches
		tmp[tmp == tmp.min()] = -9 #黑色背景区域
	return tmp

def crop_ceter(img,croph,cropw):   
	#for n_slice in range(img.shape[0]):
	height,width = img[0].shape 
	starth = height//2-(croph//2)
	startw = width//2-(cropw//2)        
	return img[:,starth:starth+croph,startw:startw+cropw]

def gen_hgg_npy(hgg_path_list:list,output_image_path,output_mask_path:str):
	for hgg_path in hgg_path_list:
		base_path = os.path.basename(hgg_path)
		# #获取每个病例的四个模态及Mask的路径
		flair_image = os.path.join(hgg_path,base_path+flair_name)
		t1_image = os.path.join(hgg_path,base_path+t1_name)
		t1ce_image = os.path.join(hgg_path,base_path+t1ce_name)
		t2_image = os.path.join(hgg_path,base_path+t2_name)
		mask_image = os.path.join(hgg_path,base_path+mask_name)
		#获取每个病例的四个模态及Mask数据
		flair_src = sitk.ReadImage(flair_image, sitk.sitkInt16)
		t1_src = sitk.ReadImage(t1_image, sitk.sitkInt16)
		t1ce_src = sitk.ReadImage(t1ce_image, sitk.sitkInt16)
		t2_src = sitk.ReadImage(t2_image, sitk.sitkInt16)
		mask = sitk.ReadImage(mask_image, sitk.sitkUInt8)
		#GetArrayFromImage()可用于将SimpleITK对象转换为ndarray
		flair_array = sitk.GetArrayFromImage(flair_src)
		t1_array = sitk.GetArrayFromImage(t1_src)
		t1ce_array = sitk.GetArrayFromImage(t1ce_src)
		t2_array = sitk.GetArrayFromImage(t2_src)
		mask_array = sitk.GetArrayFromImage(mask)
		#对四个模态分别进行标准化,由于它们对比度不同
		flair_array_nor = normalize(flair_array)
		t1_array_nor = normalize(t1_array)
		t1ce_array_nor = normalize(t1ce_array)
		t2_array_nor = normalize(t2_array)
		#裁剪(偶数才行)
		flair_crop = crop_ceter(flair_array_nor,160,160)
		t1_crop = crop_ceter(t1_array_nor,160,160)
		t1ce_crop = crop_ceter(t1ce_array_nor,160,160)
		t2_crop = crop_ceter(t2_array_nor,160,160)
		mask_crop = crop_ceter(mask_array,160,160) 
		#切片处理,并去掉没有病灶的切片
		for n_slice in range(flair_crop.shape[0]):
			if np.max(mask_crop[n_slice,:,:]) != 0:
				maskImg = mask_crop[n_slice,:,:]

				FourModelImageArray = np.zeros((flair_crop.shape[1],flair_crop.shape[2],4),float)
				flairImg = flair_crop[n_slice,:,:]
				flairImg = flairImg.astype(float)
				FourModelImageArray[:,:,0] = flairImg
				t1Img = t1_crop[n_slice,:,:]
				t1Img = t1Img.astype(float)
				FourModelImageArray[:,:,1] = t1Img
				t1ceImg = t1ce_crop[n_slice,:,:]
				t1ceImg = t1ceImg.astype(float)
				FourModelImageArray[:,:,2] = t1ceImg
				t2Img = t2_crop[n_slice,:,:]
				t2Img = t2Img.astype(float)
				FourModelImageArray[:,:,3] = t2Img       
				
				imagepath = os.path.join(output_image_path,base_path+ "_" + str(n_slice) + ".npy")
				maskpath = os.path.join(output_mask_path,base_path+ "_" + str(n_slice) + ".npy")
				np.save(imagepath,FourModelImageArray) #(160,160,4) float dtype('float64')
				np.save(maskpath,maskImg)# (160, 160) dtype('uint8') 值为0 1 2 4


if __name__ == '__main__':
	dataPrePath="/Users/zhi/Program/HTMLProgram/github.com/feiquan123/auto_seg_hippocampus/service/testdata"
	print(data_pre(dataPrePath))