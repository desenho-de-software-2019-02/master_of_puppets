
from services.base_controller import Strategy

from flask_restplus import reqparse


class ItemController(Strategy):
    def set_new_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('description', required=True)
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('price', type=int, required=True)
        self.parser.add_argument('weight', type=int, required=True)

        return self.parser


    def set_edit_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('description', required=False)
        self.parser.add_argument('name', required=False)
        self.parser.add_argument('price', type=int, required=False)
        self.parser.add_argument('weight', type=int, required=False)

        return self.parser



