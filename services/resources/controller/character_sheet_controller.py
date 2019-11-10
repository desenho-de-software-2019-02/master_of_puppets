
from flask_restplus import reqparse
from base.controller import Strategy
from models.character_sheet import CharacterSheet, ConcreteCharacterMemento
from datetime import datetime

class CharacterSheetController(Strategy):
    def set_new_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('character_class')
        self.parser.add_argument('charisma')
        self.parser.add_argument('constitution')
        self.parser.add_argument('description')
        self.parser.add_argument('dexterity')
        self.parser.add_argument('experience')
        self.parser.add_argument('hit_points')
        self.parser.add_argument('intelligence')
        self.parser.add_argument('items', action='append')
        self.parser.add_argument('level')
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('owner')
        self.parser.add_argument('race')
        self.parser.add_argument('skills', action='append')
        self.parser.add_argument('strength')
        self.parser.add_argument('wisdom')

        return self.parser


    def set_edit_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('character_class')
        self.parser.add_argument('charisma')
        self.parser.add_argument('constitution')
        self.parser.add_argument('description')
        self.parser.add_argument('dexterity')
        self.parser.add_argument('experience')
        self.parser.add_argument('hit_points')
        self.parser.add_argument('intelligence')
        self.parser.add_argument('items', action='append')
        self.parser.add_argument('level')
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('owner')
        self.parser.add_argument('race')
        self.parser.add_argument('strength')
        self.parser.add_argument('wisdom')

        return self.parser

    @staticmethod
    def new_memento(identifier):
        character_sheet = CharacterSheet.objects.get(id=identifier) 
        memento = ConcreteCharacterMemento()
        
        memento.hit_points = character_sheet.hit_points
        memento.level = character_sheet.level
        memento.experience = character_sheet.experience
        memento.strength = character_sheet.strength
        memento.dexterity = character_sheet.dexterity
        memento.constitution = character_sheet.constitution
        memento.intelligence = character_sheet.intelligence
        memento.wisdom = character_sheet.wisdom
        memento.charisma = character_sheet.charisma
        memento.skills = character_sheet.skills
        memento.items = character_sheet.items
        memento.date = str(datetime.now())[:19]
        memento.save()

        return loads(memento.to_json())

    @staticmethod
    def memento_backup(identifier, memento_identifier):
        """
        Deletes a character memento given its id
        """
        character_sheet = CharacterSheet.objects.get(id=identifier)
        memento = ConcreteCharacterMemento.objects.get(id=memento_identifier)
        
        character_sheet.hit_points = memento.hit_points
        character_sheet.level = memento.level
        character_sheet.experience = memento.experience
        character_sheet.strength = memento.strength
        character_sheet.dexterity = memento.dexterity
        character_sheet.constitution = memento.constitution
        character_sheet.intelligence = memento.intelligence
        character_sheet.wisdom = memento.wisdom
        character_sheet.charisma = memento.charisma
        character_sheet.skills = memento.skills
        character_sheet.items = memento.items

        character_sheet.save()
        memento.delete()
        
        return loads(character_sheet.to_json())
class CharacterMementoController:
    def __init__(self, request):
        self.request = request 

    @staticmethod
    def list():
        """
        Makes a query to list all characters
        """

        list_of_characters_mementoes = list(map(lambda charactermemento: loads(charactermemento.to_json() ), ConcreteCharacterMemento.objects.all()))
        return list_of_characters_mementoes

    @staticmethod
    def get_element_detail(identifier):
        """
        Returns a character memento matching the given id
        """
        return ConcreteCharacterMemento.objects.get(id=identifier).to_json()
    