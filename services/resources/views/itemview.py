from flask_restplus import Namespace, Resource

api = Resource(namespace='item')


@api.route('/items/add')
class ItemCreate(Resource):
    pass

@api.route('/items/list')
class ItemList(Resource):
    pass

@api.route('/items/detail/<int:pk>')
class ItemDetail(Resource):
    pass

@api.route('/items/delete/<int:pk>')
class ItemDelete(Resource):
    pass
