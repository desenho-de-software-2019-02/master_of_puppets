import json
from flask_restplus import Namespace, Resource
# from flask import request, jsonify

from controller.dice_controller import DiceController

api = Namespace('dice', description='Dice namespace')


@api.route('/<string:pattern>')
class DiceDetail(Resource):
    @api.doc("Get dice toss values")
    def get(self, pattern):
        controller = DiceController()
        result = controller.roll(pattern)

        return result
