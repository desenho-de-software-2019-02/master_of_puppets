import json
from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify
from mongoengine import DoesNotExist, ValidationError

from controller.character_sheet_controller import CharacterSheetController, CharacterMementoController

from models.character_sheet import CharacterSheet

api = Namespace('character_sheet', description='Character Sheet namespace')


def get_controller():
	controller = CharacterSheetController(model=CharacterSheet, request=request)
	return controller
    
character_model = api.model('Character', {
    'character_class': fields.String(required=True, description='Character\'s Class id'),
    'charisma': fields.Integer(required=True, description='Character\'s charisma id'),
    'constitution': fields.Integer(required=True, description='Character\'s constitution id'),
    'description': fields.String(description='Character\'s description'),
    'dexterity': fields.Integer(required=True, description='Character\'s dexterity id'),
    'experience': fields.Float(required=True, description='Character\'s experience points'),
    'hit_points': fields.Integer(required=True, description='Character\'s hit points'),
    'intelligence': fields.Integer(required=True, description='Character\'s intelligence id'),
    'items': fields.List(fields.String(), description='List of Character\'s items'),
    'level': fields.Integer(required=True, description='Character\'s level'),
    'name': fields.String(required=True, description='Character\'s name'),
    'owner': fields.String(required=True, description='Character\'s owner id'),
    'race': fields.String(required=True, description='Character\'s Race id'),
    'skills': fields.List(fields.String(), description='List of Character\'s skills'),
    'strength': fields.Integer(required=True, description='Character\'s strength id'),
    'wisdom': fields.Integer(required=True, description='Character\'s wisdom id'),
})

@api.route('/')
class CharacterList(Resource):
    @api.doc("Character List")
    def get(self):
        controller = get_controller()
        query = controller.list_elements()

        return jsonify(query)

    @api.doc("Character creation")
    @api.expect(character_model)
    def post(self):
        controller = get_controller()
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
        controller = get_controller()

        try:
            character = controller.get_element_detail(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Character with id {} does not exist".format(id))

        return json.loads(character)

    @api.doc("Update a character", params={'id': param})
    @api.expect(character_model)
    def put(self, id):
        controller = get_controller()

        try:
            new_character = controller.edit(id)
        except (DoesNotExist, ValidationError): 
            api.abort(400, "Charcter with id {} does not exist".format(id))

        return new_character

    @api.doc("Delete a character", params={'id': param})
    def delete(self, id):
        controller = get_controller()
        deleted = controller.delete(id)

        return deleted

@api.route('/<string:id>/backup')
@api.response(200, 'Success')
@api.response(400, 'Character not found')
@api.param('id', 'Character identifier')
class CharacterMementoCreation(Resource):
    param = "An string that represents the character's id"
    
    @api.doc("Update a character", params={'id': param})
    def post(self, id):   
        controller = get_controller()

        try:
            new_memento = controller.new_memento(id)
        except (DoesNotExist, ValidationError): 
            api.abort(400, "Character with id {} does not exist".format(id))

        return new_memento

@api.route('/<string:id>/undo/<string:memento_id>')
@api.response(200, 'Success')
@api.response(400, 'Character not found')
@api.param('id', 'Character identifier')
@api.param('memento_id', 'Character memento identifier')
class CharacterMementoBackup(Resource):
    param1 = "An string that represents the character's id"
    param2 = "An string that represents the character memento's id"
    
    @api.doc("Update a character", params={'id': param1,'memento_id': param2})
    def post(self, id, memento_id):   
        controller = get_controller()

        try:
            new_memento = controller.memento_backup(id, memento_id)
        except (DoesNotExist, ValidationError): 
            api.abort(400, "Charcter with id {} does not exist".format(id))

        return new_memento


@api.route('/memento')
class CharacterMementoList(Resource):
    @api.doc("Character memento List")
    def get(self):
        controller = CharacterMementoController(request)
        query = controller.list_elements()

        return jsonify(query)

@api.route('/memento/<string:id>')
@api.response(200, 'Success')
@api.response(400, 'Character not found')
@api.param('id', 'Character identifier')
class CharacterMementoDetail(Resource):
    param = "An string that represents the character memento's id"

    @api.doc("Get information of a specific charcter", params={'id': param})
    @api.response(400, 'Character memento not found')
    def get(self, id):
        controller = CharacterMementoController(request)

        try:
            character = controller.get_element_detail(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Character memento with id {} does not exist".format(id))

        return json.loads(character)
