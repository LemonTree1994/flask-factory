from flask import Blueprint, current_app, request

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.before_request
def before_query():
    current_app.logger.info(f'before request auth {request.method} {request.path}')

from . import login