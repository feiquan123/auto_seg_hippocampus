from error_code import SUCCESS


def data_test(dataPreOutPutPath:str)->dict:
	dataTestOutputPath = '/tmp/data_test_output'

	data = {
		"Unet": {
			"name": "Unet",
			"path": dataTestOutputPath + "/Unet",
		},
		"ResUnet": {
			"name": "ResUnet",
			"path": dataTestOutputPath + "/ResUnet",
		},
		"MMIgan": {
			"name": "MMIgan",
			"path": dataTestOutputPath + "/MMIgan",
		}
	}
	re = SUCCESS.with_data(data)
	return re