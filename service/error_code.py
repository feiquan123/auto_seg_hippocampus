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
