from flask_restplus import reqparse
from services.strategy import Strategy

class ItemController(Strategy):
    def set_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('description', required=True)
        self.parser.add_argument('price', type=int, required=True)
        self.parser.add_argument('weight', type=int, required=True)
        return self.parser
