from json import dumps, loads
from models.klass import Klass

from flask_restplus import reqparse


class ClassController:
    def __init__(self, request):
        self.request = request

    def new(self):
        """
        Creates a new class
        """
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('description', required=True)
        parser.add_argument('exclusive_skills', type=list, required=True)
        parser.add_argument('effects', type=list, required=True)
        parser.add_argument('restrictions', type=list, required=True)
        parse_result = parser.parse_args(req=self.request)

        # Document.from_json() gets a string as an argument, so we need to use `json.dumps()` here
        Klass.from_json(dumps(parse_result)).save()

        return parse_result

    @staticmethod
    def list():
        """
        Makes a query to list all classes
        """

        list_of_items = list(map(lambda klass: loads(klass.to_json()), Klass.objects.all()))
        return list_of_items

    @staticmethod
    def get_element_detail(identifier):
        """
        Returns a class matching the given id
        """
        return Klass.objects.get(id=identifier).to_json()

    def edit(self, identifier):
        """
        Edits a class given its id
        """
        klass = Klass.objects.get(id=identifier)

        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('description', required=True)
        parser.add_argument('exclusive_skills', type=list, required=True)
        parser.add_argument('effects', type=list, required=True)
        parser.add_argument('restrictions', type=list, required=True)
        parse_result = parser.parse_args(req=self.request)

        no_docs_updated = klass.update(**parse_result)

        if no_docs_updated == 1:  # the row was updated successfully
            return loads(klass.to_json())

    @staticmethod
    def delete(identifier):
        """
        Deletes an class given its id
        """
        target = Klass.objects.get(id=identifier)
        target_data = loads(target.to_json())

        target.delete()

        return target_data