"""manage and register all api here

# app.register_blueprint(index) equals app.register_blueprint(index, url_prefix="")
# if using app.register_blueprint(index, url_prefix="/"), api may could not receive request.
"""


def register_apis(app):
    from .index import bp as index
    app.register_blueprint(index)

