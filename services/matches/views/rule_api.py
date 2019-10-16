import json
from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify
from mongoengine import DoesNotExist, ValidationError

from controller.rule_controller import RuleController

api = Namespace('rules', description='Rules namespace')


rule_model = api.model('Item', {
    'name': fields.String(required=True, description='Item name'),
    'description': fields.String(required=True, description='Item description'),
    'price': fields.Float(required=True, description='Item price'),
    'weight': fields.Float(required=True, description='Item weight')
})

@api.route('/')
class RuleList(Resource):
    @api.doc("Rule List")
    def get(self):
        controller = RuleController(request)
        query = controller.list()

        return jsonify(query)

    @api.doc("Rule creation")
    # @api.expect(item_model)
    # @api.marshal_with(item_model)
    def post(self):
        controller = RuleController(request)
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
        controller = RuleController(request)

        try:
            rule = controller.get_element_detail(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Item with id {} does not exist".format(id))

        return json.loads(rule)

    @api.doc("Update an rule", params={'id': param})
    # @api.expect(rule_model)
    def put(self, id):
        controller = RuleController(request)

        try:
            new_rule = controller.edit(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Item with id {} does not exist".format(id))

        return new_rule

    @api.doc("Delete an Rule", params={'id': param})
    def delete(self, id):
        controller = RuleController(request)
        deleted = controller.delete(id)

        return deleted
