"""
manage and register all api here
"""

def register_apis(app):

    from .index import index_blueprint
    app.register_blueprint(index_blueprint,url_prefix="/")

    from .auth import auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix="/auth")