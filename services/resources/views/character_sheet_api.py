import json
from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify
from mongoengine import DoesNotExist, ValidationError

from controller.character_sheet_controller import CharacterSheetController



api = Namespace('character_sheet', description='Character Sheet namespace')


character_model = api.model('Character', {
    'name': fields.String(required=True, description='Character\'s name'),
    'description': fields.String(description='Character\'s description'),
    'hit_points': fields.Integer(required=True, description='Character\'s hit points'),
    'level': fields.Integer(required=True, description='Character\'s level'),
    'experience': fields.Float(required=True, description='Character\'s experience points'),
    'strength': fields.Integer(required=True, description='Character\'s strength id'),
    'desterity': fields.Integer(required=True, description='Character\'s desterity id'),
    'costitution': fields.Integer(required=True, description='Character\'s costitution id'),
    'intelligence': fields.Integer(required=True, description='Character\'s intelligence id'),
    'wisdom': fields.Integer(required=True, description='Character\'s wisdom id'),
    'charisma': fields.Integer(required=True, description='Character\'s charisma id'),
    'klass': fields.String(required=True, description='Character\'s Class id'),
    'race': fields.String(required=True, description='Character\'s Race id'),
    'items': fields.List(fields.String(), description='List of Character\'s items'),
    'skills': fields.List(fields.String(), description='List of Character\'s skills'),
    'owner': fields.String(required=True, description='Character\'s owner id'),
})

@api.route('/')
class CharacterList(Resource):
    @api.doc("Character List")
    def get(self):
        controller = CharacterSheetController(request)
        query = controller.list()

        return jsonify(query)

    @api.doc("Character creation")
    @api.expect(character_model)
    def post(self):
        controller = CharacterSheetController(request)
        args = controller.new()

        return args

@api.route('/<string:id>')
@api.response(200, 'Success')
@api.response(400, 'Character not found')
@api.param('id', 'Character identifier')
class CharacterDetail(Resource):
    param = "An string that represents the character's id"

    @api.doc("Get information of a specific charcter", params={'id': param})
    @api.response(400, 'Character not found')
    def get(self, id):
        controller = CharacterSheetController(request)

        try:
            character = controller.get_element_detail(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Character with id {} does not exist".format(id))

        return json.loads(character)

    @api.doc("Update a character", params={'id': param})
    @api.expect(character_model)
    def put(self, id):
        controller = CharacterSheetController(request)

        try:
            new_character = controller.edit(id)
        except (DoesNotExist, ValidationError): 
            api.abort(400, "Charcter with id {} does not exist".format(id))

        return new_character

    @api.doc("Delete a character", params={'id': param})
    def delete(self, id):
        controller = CharacterSheetController(request)
        deleted = controller.delete(id)

        return deleted
