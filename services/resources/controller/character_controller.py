from models.character import Character
from json import dumps, loads

from flask_restplus import reqparse


class CharacterController():
    def __init__(self, request):
        self.request = request
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name')
        self.parser.add_argument('description')
        self.parser.add_argument('hit_points', type=int)
        self.parser.add_argument('level', type=int)
        self.parser.add_argument('experience')
        self.parser.add_argument('attributes')
        self.parser.add_argument('race')
        self.parser.add_argument('character_class')
        self.parser.add_argument('skills')
        self.parser.add_argument('items')
        self.parser.add_argument('owner')

    def new(self):
        """
        Creates a new character given the request payload
        """

        parse_result = self.parser.parse_args(req=self.request)
        Character.from_json(dumps(parse_result)).save()

        return parse_result

    def edit(self, identifier):
        """
        Edits a character given its uid
        """
        character = Character.objects.get(id=identifier)

        parse_result = self.parser.parse_args(req=self.request)

        no_docs_updated = character.update(**parse_result)

        if no_docs_updated == 1:  # the row was updated successfully
            return loads(character.to_json())

    @staticmethod
    def delete(uid):
        """
        Deletes a character given its id
        """
        target = Character.objects.get(id=uid)
        target_data = loads(target.to_json())
        target.delete()

        return target_data

    @staticmethod
    def list():
        """
        Makes a query listing all characters
        """
        character_list = list(map(lambda character: loads(
            character.to_json()), Character.objects.all()))

        return character_list

    @staticmethod
    def show(uid):
        """
        """
        return Character.objects.get(id=uid)
