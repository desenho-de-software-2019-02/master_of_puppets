import json
from flask_restplus import Namespace, Resource, fields, Api
from flask import request, jsonify, Flask

from mongoengine import DoesNotExist
from mongoengine import ValidationError

from controller.character_class_controller import CharacterClassController
from models.character_class import CharacterClass

api = Namespace('character classes', description='classes of master of puppets namespace')


def get_controller():
	controller = CharacterClassController(model=CharacterClass, request=request)
	return controller


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
    @api.doc(description = "Post to list_elements classes.")
    def get(self):
        controller = get_controller()
        result = controller.list_elements()
        return jsonify(result)

    @api.doc(description = "Post to create class.")
    @api.expect(create)
    def post(self):
        data = request.get_json()
        controller = get_controller()
        result = controller.new()

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
        controller = get_controller()
        result = controller.delete(data['_id'])
        return result


    @api.doc('update', 
        description = "Post to update class.", params={'id':param})
    @api.expect(update)
    @api.response(200, 'Success')
    @api.response(400, 'Class not found')
    
    def put(self, id):
        controller = get_controller()

        try: 
            new_class = controller.edit(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Class with id {} does not exist".format(id))
        

        return new_class

    @api.doc("Get information of a specific class", params={'id': param})
    @api.response(200, 'Success')
    @api.response(400, 'Class not found')
    def get(self, id):
        controller = get_controller()

        try:
            get_class = controller.get_element_detail(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Class with id {} does not exist".format(id))

        return json.loads(get_class)


