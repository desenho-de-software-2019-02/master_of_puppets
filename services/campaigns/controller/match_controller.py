from json import dumps, loads
from models.match import Match

from flask_restplus import reqparse


class MatchController:
    def __init__(self, request):
        self.request = request

    def new(self):
        """
        Creates a new match
        """
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('events', type=list)
        parser.add_argument('date', required=True)
        parser.add_argument('description')

        parse_result = parser.parse_args(req=self.request)

        # Document.from_json() gets a string as an argument, so we need to use `json.dumps()` here
        Match.from_json(dumps(parse_result)).save()

        return parse_result

    @staticmethod
    def list():
        """
        Makes a query to list all matches
        """

        list_of_matches = list(map(lambda match: loads(match.to_json()), Match.objects.all()))
        return list_of_matches

    @staticmethod
    def get_element_detail(identifier):
        """
        Returns an match campaigning the given id
        """
        return Match.objects.get(id=identifier).to_json()

    def edit(self, identifier):
        """
        Edits an match given its id
        """
        match = Match.objects.get(id=identifier)

        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('events', type=list)
        parser.add_argument('date', required=True)
        parser.add_argument('description')
        parse_result = parser.parse_args(req=self.request)

        no_docs_updated = match.update(**parse_result)

        if no_docs_updated == 1:  # the row was updated successfully
            return loads(match.to_json())

    @staticmethod
    def delete(identifier):
        """
        Deletes an match given its id
        """
        target = Match.objects.get(id=identifier)
        target_data = loads(target.to_json())

        target.delete()

        return target_data
