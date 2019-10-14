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

    @staticmethod
    def list():
        """
        Makes a query to list all items
        """

        list_of_items = list(
            map(lambda item: loads(item.to_json()), Item.objects.all()))
        return list_of_items

    @staticmethod
    def get_element_detail(identifier):
        """
        Returns an item matching the given id
        """
        return Item.objects.get(id=identifier).to_json()

    def edit(self, identifier):
        """
        Edits an item given its id
        """
        item = Item.objects.get(id=identifier)

        parser = reqparse.RequestParser()
        parser.add_argument('name', required=False)
        parser.add_argument('description', required=False)
        parser.add_argument('price', type=int, required=False)
        parser.add_argument('weight', type=int, required=False)
        parse_result = parser.parse_args(req=self.request)

        no_docs_updated = item.update(**parse_result)

        if no_docs_updated == 1:  # the row was updated successfully
            return loads(item.to_json())

    @staticmethod
    def delete(identifier):
        """
        Deletes an item given its id
        """
        target = Item.objects.get(id=identifier)
        target_data = loads(target.to_json())

        target.delete()

        return target_data
