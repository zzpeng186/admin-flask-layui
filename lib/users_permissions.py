from flask import request, jsonify


def check_user_token(func):
    """
    判断用户ip地址和是否登陆
    :param func:
    :return:
    """
    def inner(*args, **kwargs):
        # 判断是否登录
        if request.remote_addr != '127.0.0.1':
            print(request.remote_addr)
            data_dict = {'code': 0, 'msg': 'error', 'count': 100}
            return jsonify(data_dict)
        return func(*args, **kwargs)

    return inner