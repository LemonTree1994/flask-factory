from flask import current_app, request
from functools import wraps



def check_login(func):
    @wraps(func)
    def wapper(*args, **kwargs):
        data = request.args or request.json or request.form
        # check
        return func(*args, **kwargs)
    return wapper
