
from base.controller import BaseController
from models.character import Character
from flask_restplus import reqparse
import requests
from json import loads

class CharacterController(BaseController):

    def set_edit_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('character_sheet', required=False)
        self.parser.add_argument('user', required=False)

        return self.parser

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