from flask import current_app, request
from functools import wraps

from app.models import Session, User

def check_login(func):
    @wraps(func)
    def wapper(*args, **kwargs):
        data = request.args or request.json or request.form
        sessionid = data.get('sessionid')
        if not sessionid:
            return 'no login', 401
        session = Session.get_by_id(sessionid)
        if not session:
            return 'no login', 401
        user = session.user_from_session
        if not user.active:
            return 'user blocked', 401
    return wapper
