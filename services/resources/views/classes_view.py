from flask_restplus import Namespace, Resource, fields
from core.classes_controller import controllerClasses
from flask import request, jsonify

api = Namespace('classes', description='classes of master of puppets')

create = api.model('create', {
    "name":fields.String(),
    "description":fields.String(),
    "effects": fields.List(fields.String),
    "restrictions": fields.List(fields.String),
    "exclusiveSkills": fields.List(fields.String)
},
)

delete = api.model('delete', {
    "_id":fields.String()
})

update = api.model('update', {
    "_id":fields.String(),
    "name":fields.String(),
    "description":fields.String(),
    "exclusiveSkills": fields.List(fields.String),
    "effects": fields.List(fields.String),
    "restrictions": fields.List(fields.String)
})

# @api.route('')
# class ClassList(Resource):
#     @api.doc('asdaslkdnasmflsdçlam')
#     def get(self):
#         return 'get_classes'

#     def post(self):
#         return 'post_classes'

@api.route('/create')
class ClassCreate(Resource):
    @api.doc('create', 
        description = "Post to create class.")
    @api.expect(create)
    # def get(self):
    #     return 'only create'

    def post(self):
        data = request.get_json()
        result = controllerClasses.validate_new_class_to_model(data)

        return result

@api.route('/read')
class ClassRead(Resource):
    @api.doc('asdaslkdnasmflsdçlam')
    def get(self):
        return controllerClasses.get_class()

    # def post(self):
    #     return "only read"

@api.route('/update', methods=['PUT'])
class ClassUpdate(Resource):
    
    @api.expect(update)
    # def get(self):
    #     return classes_controller.class_info(data)
   
    def put(self):
        data = request.get_json()
        return controllerClasses.update_class(data)

@api.route('/delete', methods=['DELETE'])
class ClassDelete(Resource):
    @api.expect(delete)
    @api.doc('delete', 
        description = "Post to delete class.")
    # def get(self, data):
    #     return "delete get"
   
    def delete(self):
        data = request.get_json()
        return controllerClasses.delete_class(data)

