from error_code import SUCCESS


def data_pre(dataPrePath:str)->dict:
	base = '/tmp/data_pre_output'
	re = SUCCESS.with_data({
		'dataPreOutPutPath':base +'/'+dataPrePath
	})
	return re