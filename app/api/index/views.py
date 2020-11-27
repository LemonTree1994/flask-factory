from flask_restful import Resource


class HelloWorld(Resource):
    def get(self):
        return "The best way to predict the future is to invent it."


class HomePage(Resource):
    def get(self, id):
        if not id:
            id = 0
        return f"You're in page {id}"
