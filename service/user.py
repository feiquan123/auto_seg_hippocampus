from error_code import ERROR_ACCOUNT_PASSWORD_INCORRECT,SUCCESS,ERROR_ILLEGAL_TOKEN

tokens = {
    "admin": {
        "token": 'admin-token',
        "password" :"admin_pwd"
    },
    "editor": {
        "token": 'editor-token',
        "password":"editor_pwd"
    }
}

users = {
    'admin-token': {
        "roles": ['admin'],
        "introduction": '我是超级管理员',
        "avatar": 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fitem%2F201412%2F14%2F20141214212532_2yPBt.thumb.400_0.gif&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1648436644&t=94060b1a28739f17f6eecc52c8a7d4eb',
        "name": '管理员'
    },
    'editor-token': {
        "roles": ['editor'],
        "introduction": '我是编辑员',
        "avatar": 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fitem%2F201903%2F04%2F20190304080638_ytizj.thumb.400_0.gif&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1648436911&t=91295abc5b3fb89949d06734e0724453',
        "name": '编辑员'
    }
}

def user_login(username, password:str)->dict:
    token = tokens.get(username,None)
    if token is None:
        return ERROR_ACCOUNT_PASSWORD_INCORRECT.__dict__()

    if password != token['password']:
        return ERROR_ACCOUNT_PASSWORD_INCORRECT.__dict__()

    re = SUCCESS.with_data({
        'token' : token['token']
    })
    return re
    


def user_info(token:str) -> dict:
    info = users.get(token,None)
    if info is None:
        return ERROR_ILLEGAL_TOKEN.__dict__()
    
    return SUCCESS.with_data(info)


def user_logout()->dict:
    return SUCCESS.__dict__()