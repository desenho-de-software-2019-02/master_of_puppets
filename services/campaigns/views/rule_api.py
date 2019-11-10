import json
from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify
from mongoengine import DoesNotExist, ValidationError

from controller.rule_controller import RuleController

from models.rule import Rule
from services.base_controller import BaseController
api = Namespace('rules', description='Rules namespace')


def get_controller():
	controller = BaseController(strategy=RuleController(), model=Rule, request=request)
	return controller



rule_model = api.model('Rule', {
    'name': fields.String(required=True, description='Rule name'),
    'description': fields.String( description='Rule description'),
    'character_classes': fields.List(fields.String),
    'races': fields.List(fields.String),
    'items': fields.List(fields.String),
    'skills': fields.List(fields.String),
})

@api.route('/')
class RuleList(Resource):
    @api.doc("Rule List")
    def get(self):
        controller = get_controller()
        query = controller.list()

        return jsonify(query)

    @api.doc("Rule creation")
    @api.expect(rule_model)
    def post(self):
        controller = get_controller()
        args = controller.new()

        return args


@api.route('/<string:id>')
@api.response(200, 'Success')
@api.response(400, 'Item not found')
@api.param('id', 'Item identifier')
class RuleDetail(Resource):
    param = "An integer that represents the rule's id"

    @api.doc("Get information of a specific rule", params={'id': param})
    @api.response(400, 'Rule not found')
    def get(self, id):
        controller = get_controller()

        try:
            rule = controller.get_element_detail(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Item with id {} does not exist".format(id))

        return json.loads(rule)

    @api.doc("Update an rule", params={'id': param})
    @api.expect(rule_model)
    def put(self, id):
        controller = get_controller()

        try:
            new_rule = controller.edit(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Item with id {} does not exist".format(id))

        return new_rule

    @api.doc("Delete an Rule", params={'id': param})
    def delete(self, id):
        controller = get_controller()
        deleted = controller.delete(id)

        return deleted
