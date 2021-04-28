import datetime

from .exts import db


class UserModel(db.Model):
    # __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
    # mobile_num = db.Column(db.Strin(11))


class ArticleModel(db.Model):
    # __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('user_model.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category_model.id'))
    add_time = db.Column(db.DateTime, default=datetime.date)
    # time_tree = db.Column(db.Date, default=datetime.date.month)

    author = db.relationship("UserModel", backref="articles")
    category = db.relationship("CategoryModel", backref='category')


class CategoryModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))