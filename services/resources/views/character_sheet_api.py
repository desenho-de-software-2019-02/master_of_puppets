import json
from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify
from mongoengine import DoesNotExist, ValidationError

from controller.character_sheet_controller import CharacterSheetController, CharacterMementoController



api = Namespace('character_sheet', description='Character Sheet namespace')


character_model = api.model('Character', {
    'name': fields.String(required=True, description='Character\'s name'),
    'description': fields.String(description='Character\'s description'),
    'hit_points': fields.Integer(required=True, description='Character\'s hit points'),
    'level': fields.Integer(required=True, description='Character\'s level'),
    'experience': fields.Float(required=True, description='Character\'s experience points'),
    'strength': fields.Integer(required=True, description='Character\'s strength id'),
    'dexterity': fields.Integer(required=True, description='Character\'s dexterity id'),
    'constitution': fields.Integer(required=True, description='Character\'s constitution id'),
    'inteligence': fields.Integer(required=True, description='Character\'s inteligence id'),
    'armor_class': fields.Float(required=True, description='Character\'s armor class base value'),
    'fortitude': fields.Float(required=True, description='Character\'s fortitude base value'),
    'reflex': fields.Float(required=True, description='Character\'s reflex base value'),
    'will': fields.Float(required=True, description='Character\'s will base value'),
    'wisdom': fields.Integer(required=True, description='Character\'s wisdom id'),
    'charisma': fields.Integer(required=True, description='Character\'s charisma id'),
    'klass': fields.String(required=True, description='Character\'s Class id'),
    'race': fields.String(required=True, description='Character\'s Race id'),
    'items': fields.List(fields.String(), description='List of Character\'s items'),
    'skills': fields.List(fields.String(), description='List of Character\'s skills'),
    'owner': fields.String(required=True, description='Character\'s owner id'),
})

character_put_model = api.model('Character', {
    'name': fields.String( description='Character\'s name'),
    'description': fields.String(description='Character\'s description'),
    'hit_points': fields.Integer( description='Character\'s hit points'),
    'level': fields.Integer( description='Character\'s level'),
    'experience': fields.Float( description='Character\'s experience points'),
    'strength': fields.Integer( description='Character\'s strength id'),
    'dexterity': fields.Integer( description='Character\'s dexterity id'),
    'constitution': fields.Integer( description='Character\'s constitution id'),
    'inteligence': fields.Integer( description='Character\'s inteligence id'),
    'armor_class': fields.Float( description='Character\'s armor class base value'),
    'fortitude': fields.Float( description='Character\'s fortitude base value'),
    'reflex': fields.Float( description='Character\'s reflex base value'),
    'will': fields.Float( description='Character\'s will base value'),
    'wisdom': fields.Integer( description='Character\'s wisdom id'),
    'charisma': fields.Integer( description='Character\'s charisma id'),
    'klass': fields.String( description='Character\'s Class id'),
    'race': fields.String( description='Character\'s Race id'),
    'items': fields.List(fields.String(), description='List of Character\'s items'),
    'skills': fields.List(fields.String(), description='List of Character\'s skills'),
    'owner': fields.String( description='Character\'s owner id'),
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
    @api.expect(character_put_model)
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

@api.route('/<string:id>/backup')
@api.response(200, 'Success')
@api.response(400, 'Character not found')
@api.param('id', 'Character identifier')
class CharacterMementoCreation(Resource):
    param = "An string that represents the character's id"
    
    @api.doc("Update a character", params={'id': param})
    def post(self, id):   
        controller = CharacterSheetController(request)

        try:
            new_memento = controller.new_memento(id)
        except (DoesNotExist, ValidationError): 
            api.abort(400, "Charcter with id {} does not exist".format(id))

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
        controller = CharacterSheetController(request)

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
        query = controller.list()

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
