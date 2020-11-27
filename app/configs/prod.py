from .default import *


DEBUG = False

# 数据库的配置信息
DB_USER = "root"
DB_PASSWD = "password"
# defined host name in docker-compose, use docker's dns for connection.
DB_HOST = "mysql"
DB_PORT = 3306
DB_NAME = "flask_factory"
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}:{}/{}"\
    .format(DB_USER, DB_PASSWD, DB_HOST, DB_PORT, DB_NAME)
