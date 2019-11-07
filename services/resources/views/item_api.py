import json
from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify
from mongoengine import DoesNotExist, ValidationError

from controller.item_controller import ItemController

from models.item import Item
from services.base_controller import Context
api = Namespace('items', description='Item namespace')


def get_controller():
	controller = Context(strategy=ItemController(), model=Item, request=request)
	return controller


item_model = api.model('Item', {
    'name': fields.String(required=True, description='Item name'),
    'description': fields.String(required=True, description='Item description'),
    'price': fields.Float(required=True, description='Item price'),
    'weight': fields.Float(required=True, description='Item weight')
})


@api.route('/')
class ItemList(Resource):
    @api.doc("Item list")
    def get(self):
        controller = get_controller()
        query = controller.list()

        return jsonify(query)

    @api.doc("Item creation")
    @api.expect(item_model)
    def post(self):
        controller = get_controller()
        args = controller.new()

        return args


@api.route('/<string:id>')
@api.response(200, 'Success')
@api.response(400, 'Item not found')
@api.param('id', 'Item identifier')
class ItemDetail(Resource):
    param = "A string that represents the item's id"

    @api.doc("Get information of a specific item", params={'id': param})
    @api.response(400, 'Item not found')
    def get(self, id):
        controller = get_controller()

        try:
            item = controller.get_element_detail(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Item with id {} does not exist".format(id))

        return json.loads(item)

    @api.doc("Update an item", params={'id': param})
    @api.expect(item_model)
    def put(self, id):
        controller = get_controller()

        try:
            new_item = controller.edit(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Item with id {} does not exist".format(id))

        return new_item

    @api.doc("Delete an item", params={'id': param})
    def delete(self, id):
        controller = get_controller()
        deleted = controller.delete(id)

        return deleted
