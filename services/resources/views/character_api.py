from flask_restplus import Namespace, Resource
from flask import request, jsonify
from mongoengine import DoesNotExist, ValidationError

from controller.character_controller import CharacterController
import json

api = Namespace('character', description='Character namespace')

# TODO: add namespace model structure


@api.route('/')
class CharacterList(Resource):
    @api.doc("Character list")
    def get(self):
        query = CharacterController(request).list()

        return jsonify(query)

    @api.doc("Character creation")
    def post(self):
        controller = CharacterController(request)

        try:
            data = controller.new()
        except ValueError:
            api.abort(400, "Invalid or insufficient arguments")

        return data


@api.route('/<string:id>')
@api.response(200, 'Success')
@api.response(400, 'Character not found')
@api.param('id', 'Character identifier')
class CharacterDetail(Resource):
    param = "Character identifier"

    @api.doc("Get information of a specific character", params={'id': param})
    def get(self, id):
        controller = CharacterController(request)

        try:
            character = controller.get_element_detail(id)
        except:
            api.abort(400, "Character with id {} does not exist".format(id))

        return json.loads(character)

    @api.doc("Update a character", params={'id': param})
    def put(self, id):
        controller = CharacterController(request)

        try:
            new_character = controller.edit(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Character with id {} does not exist".format(id))

        return new_character

    def delete(self, id):
        controller = CharacterController(request)
        deleted = controller.delete(id)

        return deleted
