from json import dumps, loads
from models.race import Race

from flask_restplus import reqparse


class RaceController:
    def __init__(self, request):
        self.request = request

    def new(self):
        """
        Creates a new race
        """
        parser = reqparse.RequestParser()
        parser.add_argument('name',required=True)
        parser.add_argument('description',required=True)
        parser.add_argument('restrictions', type=list)
        parser.add_argument('exclusive_skills', type=list)
        parse_result = parser.parse_args(req=self.request)

        # Document.from_json() gets a string as an argument,
        # so we need to use `json.dumps()` here
        rs = Race.from_json(dumps(parse_result)).save()
       
        return "{}".format(rs.id)

    @staticmethod
    def list():
        """
        Makes a query to list all items
        """

        list_of_items = list(
            map(lambda race: loads(race.to_json()), Race.objects.all()))
        return list_of_items

    @staticmethod
    def get_element_detail(identifier):
        """
        Returns an race matching the given id
        """
        return Race.objects.get(id=identifier).to_json()

    def edit(self, identifier):
        """
        Edits an race given its id
        """
        race = Race.objects.get(id=identifier)

        parser = reqparse.RequestParser()
        parser.add_argument('name', required=False)
        parser.add_argument('description', required=False)
        parser.add_argument('restrictions', type=list, required=False)
        parser.add_argument('exclusive_skills', type=list, required=False)
        parse_result = parser.parse_args(req=self.request)

        no_docs_updated = race.update(**parse_result)

        if no_docs_updated == 1:  # the row was updated successfully
            return loads(race.to_json())

    @staticmethod
    def delete(identifier):
        """
        Deletes an race given its id
        """
        target = Race.objects.get(id=identifier)
        target_data = loads(target.to_json())

        target.delete()

        return target_data
