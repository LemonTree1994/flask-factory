import logging
import os


class MyConfig(object):
    PROJECT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)))
    LOG_PATH = os.path.abspath(os.path.join(PROJECT_PATH, "logs"))

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024 #16M

    # 使用的是自己定义的session
    # flask_session的配置信息
    # SECRET_KEY = "guess_what"
    # SESSION_USE_SIGNER = True # 让 cookie 中的 session_id 被加密签名处理
    # PERMANENT_SESSION_LIFETIME = 86400 # session 的有效期，单位是秒

    # 数据库的配置信息
    DB_USER = "root"
    DB_PASSWD = "password"
    # defined host name in docker-compose, use docker's dns for connection.
    DB_HOST = "mysql"
    DB_PORT = 3306
    DB_NAME = "flask_factory"
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(DB_USER, DB_PASSWD, DB_HOST, DB_PORT,
                                                                             DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def init_app(self):
        if not os.path.exists(self.config.get('LOG_PATH')):
            os.mkdir(self.config.get('LOG_PATH'))


class ProductionConfig(MyConfig):
    DEBUG = False


class DevelopmentConfig(MyConfig):
    DEBUG = True


config_map = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig,
    "default": DevelopmentConfig,
}
