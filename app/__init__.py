from flask import Flask, request
from app.config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_apscheduler import APScheduler
import os


db = SQLAlchemy()

def create_app(config_name='development'):

    # create app
    app = Flask(__name__)

    # config app
    app.config.from_object(config_map[config_name])
    config_map[config_name].init_app(app)

    # config db
    db.init_app(app)

    from app.models import db_init
    db_init(app)

    # config scheduler   alternative
    # if you have some backend work or schedule something timely, config it in config file.
    # format refers to its api.
    # scheduler = APScheduler()
    # scheduler.init_app(app)
    # scheduler.start()

    # config  Cross Origin Resource Sharing
    CORS(app, resources='/*')

    # config logging
    import logging
    import logging.handlers
    # set logger file
    file_handler = logging.handlers.TimedRotatingFileHandler(
        filename=os.path.join(app.config.get('LOG_PATH'), 'log'), backupCount=1,
        encoding='UTF-8')

    # set file logger level
    file_handler.setLevel(logging.INFO)
    # set logger format
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(process)d %(thread)d %(message)s')
    file_handler.setFormatter(formatter)
    # set file name format
    file_handler.suffix = '%Y%m%d.log'
    # add file handle to app
    app.logger.addHandler(file_handler)

    # set app logger level
    app.logger.setLevel(logging.INFO)

    # register all apis to app
    from app.api import register_apis
    register_apis(app)

    return app

