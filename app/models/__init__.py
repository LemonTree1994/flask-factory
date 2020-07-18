import socket
import mysql
import sqlalchemy
from app import db
from .User import User
from .Session import Session


def check_init_db(app, delete=False):
    """

    :param app:
    :param delete: if delete, then delete all data in this database, and create new model
                    else it depends on whether the table existed.
    :return:
    """

    with app.app_context():
        try:
            cursor = db.session.execute("show tables;")
            results = cursor.fetchall()
            if delete:
                db.drop_all()
                db.create_all()
                return
            if not results:
                print("create models")
                db.create_all()
                return
        except sqlalchemy.exc.InterfaceError as interfacee:
            print("sqlalchemy.exc.InterfaceError: (mysql.connector.errors.InterfaceError) 2003: Can't connect to MySQL server")
            # raise interfacee

        except Exception as e:
            raise e
