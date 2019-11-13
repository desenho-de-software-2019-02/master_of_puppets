from json import dumps, loads
from models.character import Character
from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify
import requests
from controller.damage_controller import DamageController

api = Namespace('damage_trial', description='damage namespace')

damage_model = api.model('Match', {
    'caster': fields.String(required=True, description='Object Id of attacking user'),
    'target': fields.List(fields.String(), description='Object Id of target user'),
    'skill': fields.String(description='Object Id of skill used, if any'),
    'item': fields.String(description='Object Id of item used, if any')
})

@api.route('/')
class DamageAction(Resource):
    @api.doc('Damage Action')
    @api.expect(damage_model)
    def post(self):
        controller = DamageController(request)
        result = controller.trial()
        return result