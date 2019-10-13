import json
from flask_restplus import Namespace, Resource
from flask import request, jsonify
from mongoengine import DoesNotExist, ValidationError

from controller.item_controller import ItemController

api = Namespace('items', description='Item namespace')


@api.route('/')
class ItemList(Resource):
    @api.doc("Item List")
    def get(self):
        controller = ItemController(request)
        query = controller.list()

        return jsonify(query)

    @api.doc("Item creation")
    def post(self):
        controller = ItemController(request)
        args = controller.new()

        return args


@api.route('/<string:id>')
class ItemDetail(Resource):
    param = "An integer that represents the item's id"

    @api.doc("Get information of a specific item", params={'id': param})
    def get(self, id):
        controller = ItemController(request)

        try:
            item = controller.get_element_detail(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Item with id {} does not exist".format(id))

        return json.loads(item)

    @api.doc("Update an item", params={'id': param})
    def put(self, id):
        controller = ItemController(request)

        try:
            new_item = controller.edit(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Item with id {} does not exist".format(id))

        return new_item

    @api.doc("Delete an item", params={'id': param})
    def delete(self, id):
        controller = ItemController(request)
        deleted = controller.delete(id)

        return deleted
