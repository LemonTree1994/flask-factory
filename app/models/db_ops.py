import sqlalchemy
from sqlalchemy_utils.functions import database_exists, create_database

from app import db

def db_init(app, truncate=False):
    """

    :param app:
    :param truncate: if truncate, then truncate all data in this database, and create new model.
    :return:
    """
    def create_models():
        cursor = db.session.execute("show tables;")
        results = cursor.fetchall()
        if truncate:
            db.drop_all()
            db.create_all()
            return
        if not results:
            db.create_all()
            return

    with app.app_context():
        try:
            create_models()
        except sqlalchemy.exc.InterfaceError as interfacee:
            print("sqlalchemy.exc.InterfaceError: Can't connect to MySQL server")
            # raise interfacee
        except sqlalchemy.exc.ProgrammingError as programminge:
            # print("sqlalchemy.exc.ProgrammingError: Unknown database ")
            # raise programminge
            engine = db.get_engine()
            if not database_exists(engine.url):
                create_database(engine.url)
                if database_exists(engine.url):
                    print("database not exists and created")
                else:
                    print("Can not create database ")

        except Exception as e:
            raise e

