from json import dumps, loads
from models.item import Item

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

        # Document.from_json() gets a string as an argument, so we need to use `json.dumps()` here
        Item.from_json(dumps(parse_result)).save()

        return parse_result


