from flask_restful import Api

from . import bp
from .views import HelloWorld, HomePage

api = Api(bp)

api.add_resource(HelloWorld, '/', endpoint='hello')
api.add_resource(HomePage, '/<int:id>', endpoint='home')
