import json
from flask_restplus import Namespace, Resource
from flask import request
from models.item import DoesNotExist

from controller.item_controller import ItemController

api = Namespace('items', description='Item namespace')


@api.route('/')
class ItemList(Resource):
    @api.doc("Item List")
    def get(self):
        controller = ItemController(request)
        query = controller.list()

        return query

    @api.doc("Item creation")
    def post(self):
        controller = ItemController(request)
        args = controller.new()

        return args


@api.route('/<string:item_id>')
class ItemDetail(Resource):
    param = "An integer that represents the item's id"

    @api.doc("Get information of a specific item", params={'id': param})
    def get(self, item_id):
        controller = ItemController(request)

        try:
            item = controller.get_element_detail(item_id)
        except DoesNotExist:
            api.abort(400, "Item with id {} does not exist".format(item_id))

        return json.loads(item)

    @api.doc("Update an item", params={'id': param})
    def put(self, item_id):
        controller = ItemController(request)
        new_item = controller.edit(item_id)

        return new_item

    @api.doc("Delete an item", params={'id': param})
    def delete(self, item_id):
        controller = ItemController(request)
        deleted = controller.delete(item_id)

        return deleted
