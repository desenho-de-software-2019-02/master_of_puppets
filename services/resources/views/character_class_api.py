import json
from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify

from mongoengine import DoesNotExist
from mongoengine import ValidationError

from controller.character_class_controller import CharacterClassController
from models.character_class import CharacterClass

api = Namespace('character_classes', description='classes of master of puppets namespace')

def get_controller():
	controller = CharacterClassController(model=CharacterClass, request=request)
	return controller

model_class = api.model('create', {
    "name":fields.String(),
    "description":fields.String(),
    "effects": fields.List(fields.String),
    "restrictions": fields.List(fields.String),
    "exclusive_skills": fields.List(fields.String)
})


@api.route('/')
class ClassCreate(Resource):

    @api.doc(description = "Post to list_elements classes.")
    def get(self):
        controller = get_controller()
        result = controller.list_elements()
        return jsonify(result)

    @api.doc(description = "Post to create class.")
    @api.expect(model_class)
    def post(self):
        controller = get_controller()
        result = controller.new()

        return result


@api.route('/<string:id>')
@api.response(200, 'Success')
@api.response(400, 'Race not found')
@api.param('id', 'Race identifier')
class ClassDetail(Resource):

    param = "An integer that represents the classes' id"

    @api.doc("Delete an item", params={'id': param})
    def delete(self, id):
        controller = get_controller()
        deleted = controller.delete(id)

        return deleted
    
    @api.doc('update', description = "Post to update class.", params={'id':param})
    @api.expect(model_class)
    @api.response(200, 'Success')
    @api.response(400, 'Class not found')
    def put(self, id):
        controller = get_controller()

#        try:
#        except (DoesNotExist, ValidationError):
#            api.abort(400, "Match with id {} does not exist".format(id))

        new_class = controller.edit(id)
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