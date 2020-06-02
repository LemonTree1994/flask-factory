import random
import string
from flask import current_app, request

from . import auth_blueprint
from app.models import User,Session

@auth_blueprint.route("/login",methods=["POST"])
def login():
    if not request.json:
        return 'error'
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = User.validate_user(username, password)
    if user:
        if user.active:
            session = Session.create_session(user)
            return session
        else:
            return 'blocked'
    else:
        return 'error'


@auth_blueprint.route("/logout",methods=["POST"])
def logout():
    if not request.json:
        return 'error'
    data = request.json
    sessionid = data.get('sessionid')
    session = Session.get_by_id(sessionid)
    if not session:
        return 'logout'

    session = Session.disable_session(session)
    if not session.active:
        return 'logout'

    return 'error'

@auth_blueprint.route("/regist", methods=["POST"])
def regist():
    if not request.json:
        return 'error'
    data = request.json
    if "username" in data:
        username = data["username"]
    if "password" in data:
        password = data["password"]
    if not username or not password:
        return 'error'
    if User.name_is_exist(username):
        return 'username is exist.'
    user = User(username=username, password=password)

    user = User.add_user(user)
    if user:
        return str(user)
    return 'error'