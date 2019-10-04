from flask_restplus import Namespace, Resource
from core import race_controller
from flask import request, jsonify


api = Namespace('Race', description='class relacionada a raça ')


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

        

        return "test_post"


@api.route("/create")
class raceCreate(Resource):
    def post(self):
        data = request.get_json()
        result = race_controller.create_race(data)
        return result;  


@api.route('/read')
class raceRead(Resource):
    def get(self):
        return race_controller.get_race()

@api.route('/delete')
class raceDelete(Resource):
    def post(self):
        data = request.get_json()
        result =  race_controller.delete_race(data)
        return result