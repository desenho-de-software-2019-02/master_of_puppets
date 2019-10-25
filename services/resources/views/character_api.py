from flask_restplus import Namespace, Resource, fields
from controller.character_controller import CharacterController
from flask import request, jsonify


api = Namespace('character', description='Character namespace')


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
        controller = CharacterController(request)
        query = controller.list()

        return jsonify(query)

    @api.doc("Character creation")
    @api.expect(character_model)
    def post(self):
        controller = CharacterController(request)
        args = controller.new()

        return args

@api.route('/detail/')
class CharacterDetail(Resource):
    @api.doc('asdaslkdnasmflsdçlam')
    def get(self):

        data = request.get_json()
        char_id = data["id"]

        character_controller.validate_new_character_to_model(data)

        return char_id

    def post(self):

        return "test_post"