from flask_restplus import Namespace, Resource
from core import classes_controller
from flask import request, jsonify

api = Namespace('classes', description='classes of master of puppets')


@api.route('')
class ClassList(Resource):
    @api.doc('asdaslkdnasmflsdçlam')
    def get(self):
        return 'get_classes'

    def post(self):
        return 'post_classes'

@api.route('/create')
class ClassCreate(Resource):
    @api.doc('asdaslkdnasmflsdçlam')
    # def get(self):
    #     return 'only create'

    def post(self):
        data = request.get_json()
        result = classes_controller.validate_new_class_to_model(data)

        return result

@api.route('/read')
class ClassRead(Resource):
    @api.doc('asdaslkdnasmflsdçlam')
    def get(self):
        return classes_controller.get_class()

    # def post(self):
    #     return "only read"

@api.route('/update')
class ClassUpdate(Resource):
    @api.doc('asdaslkdnasmflsdçlam')
    # def get(self):
    #     return classes_controller.class_info(data)
   
    def post(self):
        data = request.get_json()
        return classes_controller.update_class(data)

@api.route('/delete')
class ClassDelete(Resource):
    @api.doc('asdaslkdnasmflsdçlam')
    # def get(self, data):
    #     return "delete get"
   
    def post(self):
        data = request.get_json()
        return classes_controller.delete_class(data)

