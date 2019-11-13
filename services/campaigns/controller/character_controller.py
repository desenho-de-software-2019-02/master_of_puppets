from json import dumps, loads
from models.character import Character

from flask_restplus import reqparse
import requests

class CharacterController:
    def __init__(self, request):
        self.request = request

    def new(self):
        """
        Creates a new character
        """
        parser = reqparse.RequestParser()
        parser.add_argument('user', required=True)
        parser.add_argument('character_sheet', required=True)
        parser.add_argument('campaign', required=True)
        parse_result = parser.parse_args(req=self.request)

        # Document.from_json() gets a string as an argument, so we need to use `json.dumps()` here
        Character.from_json(dumps(parse_result)).save()

        return parse_result

    @staticmethod
    def list():
        """
        Makes a query to list all characters
        """

        list_of_characters = list(map(lambda character: loads(character.to_json()), Character.objects.all()))
        return list_of_characters

    @staticmethod
    def get_element_detail(identifier):
        """
        Returns an character campaigning the given id
        """
        return Character.objects.get(id=identifier).to_json()

    def edit(self, identifier):
        """
        Edits an character given its id
        """
        character = Character.objects.get(id=identifier)

        parser = reqparse.RequestParser()
        parser.add_argument('user', required=False)
        parser.add_argument('character_sheet', required=False)
        parse_result = parser.parse_args(req=self.request)

        no_docs_updated = character.update(**parse_result)

        if no_docs_updated == 1:  # the row was updated successfully
            character = Character.objects.get(id=identifier)
            return loads(character.to_json())

    @staticmethod
    def delete(identifier):
        """
        Deletes an character given its id
        """
        target = Character.objects.get(id=identifier)
        target_data = loads(target.to_json())

        target.delete()

        return target_data

    @staticmethod
    def backup(identifier):
        character = Character.objects.get(id=identifier)
        r = requests.post("http://resources:5000/character_sheet/" + character.character_sheet+"/backup")
        r = r.json()
        character.character_mementoes.append(r['_id']['$oid'])
        character.save()
        return loads(character.to_json())

    @staticmethod
    def undo(identifier):
        character = Character.objects.get(id=identifier)
        
        if character.character_mementoes.__len__() == 0:
            return
        memento = character.character_mementoes.pop()
        requests.post("http://resources:5000/character_sheet/" + character.character_sheet+"/undo/" + memento)
        character.save()

        return loads(character.to_json())