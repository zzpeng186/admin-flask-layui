from flask import request, jsonify, render_template
from functools import wraps

from lib.models import LoginIpModel, WhiteIpModel, BlackIpModel
from lib.exts import db

import os

import ipdb


def get_ip_addr(ip):
    """
    判断ip归属地
    :param ip:
    :return: str
    """
    ipip_db_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(ipip_db_path)
    db = ipdb.City(ipip_db_path + '/data_files/ipipfree.ipdb')
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
        # ip_str = request.remote_addr
        ip_str = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        print(ip_str)
        ip_addr = get_ip_addr(ip_str)
        white_ip_obj = WhiteIpModel.query.filter(WhiteIpModel.ip == ip_str).all()
        if white_ip_obj:
            count = white_ip_obj[0].count + 1
            white_ip_obj[0].count = count
            db.session.commit()
            return func(*args, **kwargs)
        # black_ip_obj = BlackIpModel.query.filter(BlackIpModel.ip == ip_str).all()[0]
        # ip_addr = '1.1.1.1'
        if ip_addr == '本机地址 本机地址 ':
            white_ip = WhiteIpModel(ip=ip_str, ip_addr=ip_addr)
            db.session.add(white_ip)
            db.session.commit()
            return func(*args, **kwargs)
        if ip_addr != '中国 山东 济南':
            # print(request.remote_addr)
            black_ip_obj = BlackIpModel.query.filter(BlackIpModel.ip == ip_str).all()
            if black_ip_obj:
                print(black_ip_obj[0].count)
                count = black_ip_obj[0].count + 1
                black_ip_obj[0].count = count
                db.session.commit()
            else:
                black_ip = BlackIpModel(ip=ip_str, ip_addr=ip_addr)
                db.session.add(black_ip)
                db.session.commit()
            # data_dict = {'code': 0, 'msg': 'error', 'count': 100}
            return render_template('error/404.html')
            # return jsonify(data_dict)
        white_ip = WhiteIpModel(ip=ip_str, ip_addr=ip_addr)
        db.session.add(white_ip)
        db.session.commit()
        return func(*args, **kwargs)

    return inner


def check_user_token_api(func):
    """
    判断用户ip地址和是否登陆(api判断）
    :param func:
    :return:
    """
    @wraps(func)
    def inner(*args, **kwargs):
        # 判断是否登录
        ip_str = request.remote_addr
        ip_addr = get_ip_addr(ip_str)
        white_ip_obj = WhiteIpModel.query.filter(WhiteIpModel.ip == ip_str).all()
        if white_ip_obj:
            return func(*args, **kwargs)
        else:
            data_dict = {'code': 0, 'msg': 'error', 'count': 100}
            # return render_template('error/404.html')
            return jsonify(data_dict)
        # ip_addr = '1.1.1.1'
        # if ip_addr != '中国 山东 济南':
        #     # print(request.remote_addr)
        #     black_ip_obj = BlackIpModel.query.filter(BlackIpModel.ip == ip_str).all()[0]
        #     if black_ip_obj:
        #         print(black_ip_obj.count)
        #         count = black_ip_obj.count + 1
        #         black_ip_obj.count = count
        #         db.session.commit()
        #     else:
        #         black_ip = BlackIpModel(ip=ip_str, ip_addr=ip_addr)
        #         db.session.add(black_ip)
        #         db.session.commit()
        #     data_dict = {'code': 0, 'msg': 'error', 'count': 100}
        #     # return render_template('error/404.html')
        #     return jsonify(data_dict)
        # return func(*args, **kwargs)

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

get_ip_addr('1.1.1.1')