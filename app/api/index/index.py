from . import index_blueprint

@index_blueprint.route("/")
def index():
    return "The best way to predict the future is to invent it."