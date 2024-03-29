import json

class Code :
	def __init__(self, code:int, message:str):
		self.code = code
		self.message = message

	def with_data(self, data:dict)->dict:
		re = self.__dict__()
		re['data'] = data
		return re	

	def __dict__(self):
		return {
			"code":self.code,
			"message": self.message,
		}
		
	def __str__(self) -> str:
		return json.dumps(self.map(),ensure_ascii=False)
	
	

SUCCESS = Code(code=20000,message="成功")
ERROR_REQUEST_ARGS = Code(code=400099, message="请求参数错误")
ERROR_ILLEGAL_TOKEN = Code(code=50008,message="无效token")
ERROR_OTHER_CLIENTS = Code(code=50012,message="已经在其他客户端登录")
ERROR_TOKEN_Expired = Code(code=50014,message="token 过期")
ERROR_ACCOUNT_PASSWORD_INCORRECT = Code(code=60204,message='账号、密码无效')
# custom error code
# 模型预处理
ERROR_DATA_PATH_NOT_EXISTS = Code(code=70001,message="路径不存在")
ERROR_HGG_DATA_PATH_NOT_EXISTS = Code(code=70002,message="当前路径下不存在 HGG 文件夹")
ERROR_LGG_DATA_PATH_NOT_EXISTS = Code(code=70003,message="当前路径下不存在 LGG 文件夹")
ERROR_HGG_DATA_EMPTY = Code(code=70004,message="当前路径下的 HGG 子文件夹中，测试病例为空 ")
ERROR_LGG_DATA_EMPTY = Code(code=70005,message="当前路径下的 LGG 子文件夹中，测试病例为空 ")
ERROR_HGG_DATA_ARRIVE_MAX = Code(code=70006,message="当前路径下的 HGG 子文件夹中，测试病例最多为5个")
ERROR_LGG_DATA_ARRIVE_MAX = Code(code=70007,message="当前路径下的 LGG 子文件夹中，测试病例最多为5个")

# 模型测试
ERROR_IMAGE_TEST_DATA_PATH_NOT_EXISTS = Code(code=70008,message="当前路径下的 image 子文件夹不存在")
ERROR_MASK_TEST_DATA_PATH_NOT_EXISTS = Code(code=70009,message="当前路径下的 mask 子文件夹不存在")
ERROR_UNKNOWN_ARCH = Code(code=70010,message="未知的模型类型，请重新选择模型类型")
ERROR_OUTPUT_GT_TEST_DATA_EMPTY = Code(code=70011,message="测试结果路径下的 GT 子文件加数据为空")
ERROR_OUTPUT_TEST_DATA_EMPTY = Code(code=70012,message="测试结果路径下发的数据为空")