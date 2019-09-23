from flask_restplus import Namespace, Resource
from controller import character_controller
from flask import request, jsonify


api = Namespace('character', description='teste teste')


@api.route('')
class CharacterList(Resource):
    @api.doc('asdaslkdnasmflsdçlam')
    def get(self):
        return "teste"

    def post(self):
        data = request.get_json()

        new_element = {
        "nome": data["name"],
        "exemplo": data["asdlasjd"]

        }

        char_collection

        return "test_post"

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