from flask import Flask
from flask import render_template, jsonify, request

import json

from config import configs
from lib.exts import db

from lib.models import UserModel, ArticleModel, CategoryModel
from lib.users_permissions import check_user_token

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
# @check_user_token
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
    return render_template('admin_index.html')




if __name__ == '__main__':
    app.run()
