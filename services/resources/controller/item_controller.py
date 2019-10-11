from json import dumps, loads
from models.item import Item

from flask_restplus import reqparse


class ItemController:
    def __init__(self, request):
        self.request = request

    def new(self):
        """
        Creates a new item
        """
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('description', required=True)
        parser.add_argument('price', type=int, required=True)
        parser.add_argument('weight', type=int, required=True)
        parse_result = parser.parse_args(req=self.request)

        # Document.from_json() gets a string as an argument, so we need to use `json.dumps()` here
        Item.from_json(dumps(parse_result)).save()

        return parse_result

    def list(self):
        """
        Makes a query to list all items
        """
        return Item.objects.all()

    def get_element_detail(self, identifier):
        """
        Returns an Item matching the given id
        """
        return Item.objects.get(id=identifier).to_json()

    def edit(self, identifier):
        """
        Edits a Item
        """
        item = Item.objects.get(id=identifier)

        parser = reqparse.RequestParser()
        parser.add_argument('name', required=False)
        parser.add_argument('description', required=False)
        parser.add_argument('price', type=int, required=False)
        parser.add_argument('weight', type=int, required=False)
        parse_result = parser.parse_args(req=self.request)

        no_docs_updated = item.update(**parse_result)

        if no_docs_updated == 1: # the row was updated successfully
            return loads(item.to_json())

    def delete(self, identifier):
        """
        Deletes an item given it's id
        """
        target = Item.objects.get(id=identifier)
        target_data = loads(target.to_json())

        target.delete()

        return target_data
