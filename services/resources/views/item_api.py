from flask_restplus import Namespace, Resource
from flask import request

from controller import item_controller

api = Namespace('items', description='Item namespace')


@api.route('/add')
class ItemCreate(Resource):
    @api.doc("Api creation class")
    def post(self):
        data = request.get_json()

        object_id = item_controller.validate_item_json(data)

        response = {
            "name": data["name"],
            "object_id": object_id
        }

        return response


@api.route('/list')
class ItemList(Resource):
    pass

@api.route('/detail/<int:pk>')
class ItemDetail(Resource):
    pass

@api.route('/delete/<int:pk>')
class ItemDelete(Resource):
    pass
