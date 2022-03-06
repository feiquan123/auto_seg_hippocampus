from flask import Flask,request,make_response
from error_code import ERROR_REQUEST_ARGS
from user import user_login,user_info,user_logout
from data_pre import data_pre
from data_test import data_test
import json

app = Flask(__name__)

@app.route('/user/login',methods=['POST'])
def userLogin():
	data = request.get_json()
	if data is None:
		return make_response(json.dumps(ERROR_REQUEST_ARGS.__dict__()))

	username = data.get('username',None)
	if username is None:
		return make_response(json.dumps(ERROR_REQUEST_ARGS.__dict__()))

	password = data.get('password',None)
	if password is None:
		return make_response(json.dumps(ERROR_REQUEST_ARGS.__dict__()))

	resp = make_response(json.dumps(user_login(username,password)))
	return resp

@app.route("/user/info",methods=['GET'])
def userInfo():
	token = request.args.get('token',None)
	if token is None:
		return make_response(json.dumps(ERROR_REQUEST_ARGS.__dict__()))

	resp = make_response(json.dumps(user_info(token)))
	return resp

@app.route("/user/logout",methods=['POST'])
def userLogout():
	resp = make_response(json.dumps(user_logout()))
	return resp

	

@app.route('/data/pre',methods=['POST'])
def dataPre():
	data = request.get_json()
	if data is None:
		return make_response(json.dumps(ERROR_REQUEST_ARGS.__dict__()))
	
	dataPrePath = data.get('dataPrePath',None)
	if dataPrePath is None:
		return make_response(json.dumps(ERROR_REQUEST_ARGS.__dict__()))

	resp = make_response(json.dumps(data_pre(dataPrePath)))
	return resp

@app.route('/data/test',methods=['POST'])
def dataTest():
	data = request.get_json()
	if data is None:
		return make_response(json.dumps(ERROR_REQUEST_ARGS.__dict__()))
	
	dataPreOutPutPath = data.get('dataPreOutPutPath',None)
	if dataPreOutPutPath is None:
		return make_response(json.dumps(ERROR_REQUEST_ARGS.__dict__()))

	resp = make_response(json.dumps(data_test(dataPreOutPutPath)))
	return resp

	


if __name__ == "__main__":
	app.debug=True
	app.run(host="127.0.0.1",port=9529)