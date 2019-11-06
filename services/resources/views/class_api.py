import json
from flask_restplus import Namespace, Resource, fields, Api
from controller.class_controller import ClassController
from flask import request, jsonify, Flask

from mongoengine import DoesNotExist
from mongoengine import ValidationError

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
    "name":fields.String(),
    "description":fields.String(),
    "exclusive_skills": fields.List(fields.String),
    "effects": fields.List(fields.String),
    "restrictions": fields.List(fields.String)
})

@api.route('/')
class ClassCreate(Resource):
    @api.doc(description = "Post to list classes.")
    def get(self):
        instance = ClassController(request)
        result = instance.list()
        return jsonify(result)

    @api.doc(description = "Post to create class.")
    @api.expect(create)
    def post(self):
        data = request.get_json()
        instance = ClassController(request)
        result = instance.new()

        return result

@api.route('/<string:id>')
@api.response(200, 'Success')
@api.response(400, 'Race not found')
@api.param('id', 'Race identifier')
class ClassDetail(Resource):
    param = "An integer that represents the classes' id"
    @api.expect(delete)
    @api.doc('delete', 
        description = "Post to delete class.", params={'id': param})

    def delete(self, id):
        data = request.get_json()
        instance = ClassController(request)
        result = instance.delete(data['_id'])
        return result


    @api.doc('update', 
        description = "Post to update class.", params={'id':param})
    @api.expect(update)
    @api.response(200, 'Success')
    @api.response(400, 'Class not found')
    
    def put(self, id):
        instance = ClassController(request)

        try: 
            new_class = instance.edit(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Class with id {} does not exist".format(id))
        

        return new_class

    @api.doc("Get information of a specific class", params={'id': param})
    @api.response(200, 'Success')
    @api.response(400, 'Class not found')
    def get(self, id):
        instance = ClassController(request)

        try:
            get_class = instance.get_element_detail(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Class with id {} does not exist".format(id))

        return json.loads(get_class)


