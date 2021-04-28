from flask import Flask
from flask import render_template, jsonify, request

import json

from config import configs
from lib.exts import db

from lib.models import UserModel, ArticleModel, CategoryModel

app = Flask(__name__)
app.config.from_object(configs)
db.init_app(app)


@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'Hello World!'


@app.route('/api/article_list/')
def index_list():
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
    if request.method == 'GET':
        detail_id = request.args.get('id')
        article_detail = ArticleModel.query.filter(ArticleModel.id == int(detail_id))[0]
        # print(article_detail[0].content)
        # article_detail = article_obj
        article_dict = {'title': article_detail.title, 'content': article_detail.content,
                        'author': article_detail.author.username, 'category': article_detail.category.name}

        data_dict = {'code': 0, 'msg': 'success', 'data': article_dict}
        return jsonify(data_dict)



if __name__ == '__main__':
    app.run()
