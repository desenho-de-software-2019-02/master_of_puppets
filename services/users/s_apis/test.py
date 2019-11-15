from flask_restplus import Namespace, Resource

api = Namespace('test', description='teste teste')


@api.route('')
class Test(Resource):

    @api.doc('teste')
    def get(self):
        return "teste"


    def post(self):
        return "test_post"
