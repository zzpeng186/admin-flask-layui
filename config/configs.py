HOST = 'rm-m5e5mid714hcv865ceo.mysql.rds.aliyuncs.com'
PORT = '3306'
DATABASE = 'admin-flask-layui'
USERNAME = 'zpz'
PASSWORD = 'admin00!@#'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                        password=PASSWORD, host=HOST,
                                                                                        port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

