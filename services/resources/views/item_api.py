from flask_restplus import Namespace, Resource
from flask import request

from controller.item_controller import ItemController

api = Namespace('items', description='Item namespace')


@api.route('/add')
class ItemCreate(Resource):
    @api.doc("Item creation")
    def post(self):
        controller = ItemController(request)
        args = controller.check()

        return args


@api.route('/list')
class ItemList(Resource):
    pass

@api.route('/detail/<int:pk>')
class ItemDetail(Resource):
    pass

@api.route('/delete/<int:pk>')
class ItemDelete(Resource):
    pass
