from flask import Blueprint, current_app, request

index_blueprint = Blueprint("index", __name__)

@index_blueprint.before_request
def before_index():
    current_app.logger.info(f'before request index {request.method} {request.path}')

@index_blueprint.route("/")
def index():
    return "The best way to predict the future is to invent it."
