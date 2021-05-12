from flask import Flask
from flask import render_template, jsonify, request

import json
import os

from config import configs
from lib.exts import db

from lib.models import UserModel, ArticleModel, CategoryModel, LoginIpModel, BlackIpModel
from lib.users_permissions import check_user_token, get_ip_addr, check_user_token_api
from lib.server_info import get_server_info

app = Flask(__name__)
app.config.from_object(configs)
db.init_app(app)


# def check_user_token(func):
#     """
#     后端请求判断是否登录
#     :param func:
#     :return:
#     """
#     def inner(*args, **kwargs):
#         # 判断是否登录
#         # # 测试代码
#         # token = args[0].META.get('HTTP_AUTHENTICATION', '')
#         token_dict = {'65daa01eb5ae4a3f8f9cb7ec293ec0ee1a453d06': 'admin'}
#         # token = '65daa01eb5ae4a3f8f9cb7ec293ec0ee1a453d06'
#
#         # print(args)
#         if request.remote_addr != '127.0.0.1':
#             print(request.remote_addr)
#             data_dict = {'code': 0, 'msg': 'error', 'count': 100}
#             return jsonify(data_dict)
#         # token = args[0].GET.get('token', '')
#         # token = str(token)
#         # print(token)
#
#         # data_json = json.dumps(data_dict)
#
#
#
#         # print('+++++++++++', username)
#         # if username == "":
#         #     # 保存当前的url到session中
#         #     args[0].session["path"] = args[0].path
#         #     # 重定向到登录页面
#         #     return HttpResponseRedirect(reverse("login"))
#         return func(*args, **kwargs)
#
#     return inner


@app.route('/')
@check_user_token
def hello_world():
    return render_template('index.html')
    # return 'Hello World!'


@app.route('/api/article_list/')
def index_list():
    """
    文章主页列表接口
    :return:
    """
    article_obj = ArticleModel.query.order_by(ArticleModel.id.desc())
    print(article_obj)
    article_list = []
    for article_detail in article_obj:
        print(article_detail)
        article_dict = {}
        article_list.append({'id': article_detail.id, 'title': article_detail.title, 'content': article_detail.content,
                             'author': article_detail.author.username, 'category': article_detail.category.name})
    print(article_list)
    # article_list = json.dumps(article_list)
    data_dict = {'code': 0, 'msg': 'success', 'count': 100, 'data': article_list}
    # data_json = json.dumps(data_dict)
    return jsonify(data_dict)


@app.route('/api/detail', methods=['GET'])
def detail():
    """
    文章详情接口
    :return:
    """
    if request.method == 'GET':
        detail_id = request.args.get('id')
        article_detail = ArticleModel.query.filter(ArticleModel.id == int(detail_id))[0]
        # print(article_detail[0].content)
        # article_detail = article_obj
        article_dict = {'title': article_detail.title, 'content': article_detail.content,
                        'author': article_detail.author.username, 'category': article_detail.category.name,
                        'add_time': str(article_detail.add_time)}
        print(article_detail.add_time)

        data_dict = {'code': 0, 'msg': 'success', 'data': article_dict}
        return jsonify(data_dict)
    else:
        data_dict = {'code': 0, 'msg': 'error'}
        return jsonify(data_dict)


@app.route('/api/title_list/', methods=['GET'])
def title_list():
    """
    目录
    :return: list
    """
    article_obj = ArticleModel.query.order_by(ArticleModel.add_time.desc())
    article_list = []
    for article in article_obj:
        article_dict = {}
        article_dict['id'] = article.id
        article_dict['title'] = article.title
        article_dict['add_time'] = article.add_time
        article_list.append(article_dict)
    data_dict = {'code': 0, 'msg': 'success', 'data': article_list}
    return jsonify(data_dict)

# @app.route('/api/time_tree/', methods=['GET'])
# def time_tree():
#     """
#     目录-时间树
#     :return: list  [{'2021-04': [1, 2, 3]}, {'2021-03': [1, 2]]
#     """
#     article_obj = ArticleModel.query.order_by(ArticleModel.add_time.desc())
#     for article in article_obj:
#         date_month_list = str(article.add_time).split('-', 2)
#         date_month = date_month_list[0] + '-' + date_month_list[1]


@app.route('/admin/index/')
@check_user_token
def admin_index():
    ip_str = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    ip_addr = get_ip_addr(ip_str)
    login_ip = LoginIpModel(ip=ip_str, ip_addr=ip_addr)
    db.session.add(login_ip)
    db.session.commit()
    return render_template('admin_index.html')


@app.route('/admin/add_article')
@check_user_token
def add_article():
    category_obj = CategoryModel.query.all()
    context = {'category_list': category_obj}
    return render_template('add_article.html', category_list=category_obj)


@app.route('/api/admin/article_add/', methods=['POST'])
@check_user_token_api
def article_add():
    request_data = request.get_data()
    json_data = json.loads(request_data)
    print(json_data)
    title = json_data['title']
    print(title)
    category_id = int(json_data['interest'])
    content = json_data['content']
    add_time = json_data['date']
    article_obj = ArticleModel(title=title, category_id=category_id, content=content, author_id=1, add_time=add_time)
    db.session.add(article_obj)
    db.session.commit()
    return jsonify({'code': 0, 'msg': 'success'})


@app.route('/api/admin/add_image/', methods=['POST'])
@check_user_token_api
def add_image():
    # pass
    '''图片上传处理页'''
    # 【1】得到图片
    # pic = request.FILES['file']
    pic = request.files.get('file')
    print(pic.filename)
    # 【2】拼接图片保存路径+图片名
    ext = pic.filename.split('.')[-1]
    import time
    pic_name = str(int(time.time())) + '.' + ext
    time_path = time.strftime("%Y/%m/%d", time.localtime(time.time()))
    print(time_path)
    # image_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    image_path = os.path.abspath(os.path.dirname(__file__))

    pic_path = '{}/upload/{}/'.format(image_path, time_path)
    if not os.path.exists(pic_path):
        os.makedirs(pic_path)

    file_path = pic_path + pic_name
    pic.save(file_path)
    image_upload_path = '/upload/{}/{}/'.format(time_path, pic_name)
    return jsonify({'msg': 'success', 'code': 0, 'data': {'src': str(pic_path)}})

    save_path = pic_path + '{}'.format(pic_name)
    # save_path = '{}/{}/{}'.format(MEDIA_ROOT, time_path, pic_name)
    # save_path = '{}/app1/{}'.format(MEDIA_ROOT, pic_name)
    # save_path = "%s/app1/%s" % (MEDIA_ROOT, pic.name)
    # 【3】保存图片到指定路径，因为图片是2进制式，因此用wb，
    with open(save_path, 'wb') as f:
        # pic.chunks()为图片的一系列数据，它是一一段段的，所以要用for逐个读取
        for content in pic.chunks():
            f.write(content)

    # 【4】保存图片路径到数据库，此处只保存其相对上传目录的路径
    # article_obj = ArticleModel.objects.get(id=1)
    # article_obj.image_path = 'media/' + 'app1/{}'.format(pic.name)
    # article_obj.save()
    image_path = pic_path + '{}'.format(pic_name)
    # image_path = '{}'.format(MEDIA_ROOT) + '/{}/{}'.format(time_path, pic_name)
    # image_path = 'media/' + 'app1/{}'.format(pic.name)
    src = image_path
    print(src)
    # ArticleModel.objects.create(image_path='app1/%s' % pic.name)

    # 【5】别忘记返回信息
    # return HttpResponse('上传成功，图片地址：app1/%s' % pic.name)
    return HttpResponse(json.dumps({'msg': 'success', 'code': 0, 'data': {'src': str(image_path)}}))


@app.route('/api/admin/index/')
# @check_user_token_api
def admin_index_list():
    # 登陆信息
    login_ip_obj = LoginIpModel.query.order_by(LoginIpModel.id.desc()).first()
    login_ip_str = login_ip_obj.ip
    login_ip_addr = login_ip_obj.ip_addr
    # 黑名单排行
    black_ip_obj = BlackIpModel.query.order_by(BlackIpModel.count.desc()).limit(5)
    black_ip_list = []
    for black_ip_detail in black_ip_obj:
        # black_list = []
        black_list = [black_ip_detail.ip, black_ip_detail.ip_addr, black_ip_detail.count]
        # black_ip_dict[black_ip_detail.ip] = black_ip_detail.ip_addr
        black_ip_list.append(black_list)
    print(black_ip_list)
    server_detail_dict = {'login_ip': login_ip_str + ' ' + login_ip_addr, 'black_ip': black_ip_list}
    # data_list =
    data_dict = {'code': 0, 'msg': 'success', 'data': server_detail_dict}
    return jsonify(data_dict)


@app.route('/api/admin/server_info/')
# @check_user_token_api
def admin_server_info():
    server_info_dict = get_server_info()
    data_dict = {'code': 0, 'msg': 'success', 'data': server_info_dict}
    return jsonify(data_dict)


@app.route('/api/admin/title_list/')
# @check_user_token_api
def title_list_api():
    article_obj = ArticleModel.query.order_by(ArticleModel.read_num.desc()).limit(5)
    article_list = []
    for article_obj_detail in article_obj:
        article_dict = {}
        article_dict['id'] = article_obj_detail.id
        article_dict['title'] = article_obj_detail.title
        article_dict['read_num'] = article_obj_detail.read_num
        article_list.append(article_dict)
    print(article_list)
    data_dict = {'code': 0, 'msg': 'success', 'data': article_list}
    return jsonify(data_dict)


if __name__ == '__main__':
    app.run()
