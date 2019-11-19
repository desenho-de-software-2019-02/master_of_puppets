from json import dumps
from models.item import ItemFactory
from base.controller import BaseController

from flask_restplus import reqparse

class ItemController(BaseController):

    def new(self):
        """
        Creates a new item
        """
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('description', required=True)
        parser.add_argument('price', type=int, required=True)
        parser.add_argument('weight', type=int, required=True)
        parser.add_argument('weapon_type')
        parser.add_argument('armor_class_mod')
        parser.add_argument('armor_class_max')
        parser.add_argument('dmg_dice')
        parser.add_argument('proficiency')
        parser.add_argument('weapon_type')
        parse_result = parser.parse_args(req=self.request)

        # Document.from_json() gets a string as an argument, so we need to use `json.dumps()` here
        factory = ItemFactory(parse_result)
        item_class = factory.create_item()

        item_data = factory.get_data()
        item_class.from_json(dumps(item_data)).save()

        item_data['item_type'] = str(item_class)

        return item_data

    def set_edit_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('description', required=False)
        self.parser.add_argument('name', required=False)
        self.parser.add_argument('price', type=int, required=False)
        self.parser.add_argument('weight', type=int, required=False)

        return self.parser
