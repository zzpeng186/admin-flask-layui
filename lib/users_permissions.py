from flask import request, jsonify, render_template
from functools import wraps

from lib.models import LoginIpModel, WhiteIpModel, BlackIpModel
from lib.exts import db

import ipdb


def get_ip_addr(ip):
    """
    判断ip归属地
    :param ip:
    :return: str
    """
    db = ipdb.City('../data_files/ipipfree.ipdb')
    db_detail = db.find_info(str(ip), 'CN')
    ip_addr = db_detail.country_name + ' ' + db_detail.region_name + ' ' + db_detail.city_name
    print(ip_addr)
    return ip_addr
    # print(db_detail.country_name)
    #
    # print(db_detail.city_name)


def check_user_token(func):
    """
    判断用户ip地址和是否登陆
    :param func:
    :return:
    """
    @wraps(func)
    def inner(*args, **kwargs):
        # 判断是否登录
        ip_str = request.remote_addr
        ip_addr = get_ip_addr(ip_str)
        if ip_addr != '中国 山东 济南':
            # print(request.remote_addr)
            black_ip = BlackIpModel(ip_str, ip_addr)
            db.session.add(black_ip)
            db.session.commit()
            data_dict = {'code': 0, 'msg': 'error', 'count': 100}
            # return render_template('admin_index.html')
            return jsonify(data_dict)
        return func(*args, **kwargs)

    return inner


def check_user_token_backup(func):
    """
    判断用户ip地址和是否登陆
    :param func:
    :return:
    """
    @wraps(func)
    def inner(*args, **kwargs):
        # 判断是否登录
        if request.remote_addr != '127.0.0.2':
            print(request.remote_addr)
            data_dict = {'code': 0, 'msg': 'error', 'count': 100}
            return jsonify(data_dict)
        return func(*args, **kwargs)

    return inner