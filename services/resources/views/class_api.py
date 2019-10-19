from flask_restplus import Namespace, Resource, fields
from controller.class_controller import ClassController
from flask import request, jsonify

api = Namespace('classes', description='classes of master of puppets')

create = api.model('create', {
    "name":fields.String(),
    "description":fields.String(),
    "effects": fields.List(fields.String),
    "restrictions": fields.List(fields.String),
    "exclusive_skills": fields.List(fields.String)
},
)

delete = api.model('delete', {
    "_id":fields.String()
})

update = api.model('update', {
    "_id":fields.String(),
    "name":fields.String(),
    "description":fields.String(),
    "exclusive_skills": fields.List(fields.String),
    "effects": fields.List(fields.String),
    "restrictions": fields.List(fields.String)
})

@api.route('/create')
class ClassCreate(Resource):
    @api.doc('create', 
        description = "Post to create class.")
    @api.expect(create)

    def post(self):
        data = request.get_json()
        instance = ClassController(request)
        result = instance.new()

        return result

@api.route('/read')
class ClassRead(Resource):
    @api.doc('read', 
        description = "Post to read class.")

    def get(self):
        instance = ClassController(request)
        result = instance.list()
        return result

@api.route('/update', methods=['PUT'])
class ClassUpdate(Resource):
    @api.doc('update', 
        description = "Post to update class.")
    @api.expect(update)
    
    def put(self):
        data = request.get_json()
        instance = ClassController(request)
        result = instance.edit(data['_id'])
        return result

@api.route('/delete', methods=['DELETE'])
class ClassDelete(Resource):
    param = "An integer that represents the classes' id"
    @api.expect(delete)
    @api.doc('delete', 
        description = "Post to delete class.")

    def delete(self):
        data = request.get_json()
        instance = ClassController(request)
        result = instance.delete(data['_id'])
        return result
