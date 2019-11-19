from flask_restplus import Namespace, Resource, fields
from flask import request
from controller.damage_controller import DamageController

api = Namespace('damage', description='damage namespace')

damage_model = api.model('Damage Action', {
    'caster': fields.String(required=True, description='Object Id of attacking user'),
    'target': fields.String(description='Object Id of target user'),
    'skill': fields.String(description='Object Id of skill used, if any'),
    'item': fields.String(description='Object Id of item used, if any'),
    'dice_result': fields.Integer(description='The result of 1d20 rolled by the player'),
    'step': fields.Integer(description='1 or 2')

})

damage_deal = api.model('Deal Damage',{
    'caster': fields.String(required=True, description='Object Id of attacking user'),
    'target': fields.String(description='Object Id of target user'),
    'skill': fields.String(description='Object Id of skill used, if any'),
    'item': fields.String(description='Object Id of item used, if any'),
    'dice_result': fields.Integer(description='The result of damage dice rolled by the player')
})

@api.route('/')
class DamageAction(Resource):
    @api.doc('Damage Action')
    @api.expect(damage_model)
    def post(self):
        controller = DamageController(request)
        result = controller.calculate()
        return result