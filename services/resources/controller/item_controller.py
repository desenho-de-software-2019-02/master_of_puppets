from models.item import insert_new_item

from flask_restplus import reqparse


class ItemController:
    def __init__(self, request):
        self.request = request

    def check(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('description', required=True)
        parser.add_argument('price', type=int, required=True)
        parser.add_argument('weight', type=int, required=True)
        parse_result = parser.parse_args(req=self.request)

        return parse_result
