from json import dumps, loads
from flask_restplus import reqparse
from models.character_sheet import CharacterSheet
from models.character_sheet import ConcreteCharacterMemento
from datetime import datetime

class CharacterSheetController:
    def __init__(self, request):
        self.request = request
    
    def new(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('description')
        parser.add_argument('hit_points')
        parser.add_argument('level')
        parser.add_argument('experience')
        parser.add_argument('strength')
        parser.add_argument('desterity')
        parser.add_argument('costitution')
        parser.add_argument('intelligence')
        parser.add_argument('wisdom')
        parser.add_argument('charisma')
        parser.add_argument('race')
        parser.add_argument('klass')
        parser.add_argument('skills', action='append')
        parser.add_argument('items', action='append') 
        parser.add_argument('owner')
        parse_result = parser.parse_args(req=self.request)
 
        CharacterSheet.from_json(dumps(parse_result)).save()

        return parse_result

    @staticmethod
    def list():
        """
        Makes a query to list all characters
        """

        list_of_characters = list(map(lambda character: loads(character.to_json() ), CharacterSheet.objects.all()))
        return list_of_characters

    @staticmethod
    def get_element_detail(identifier):
        """
        Returns a character matching the given id
        """
        return CharacterSheet.objects.get(id=identifier).to_json()

    def edit(self, identifier):
        """
        Edits a character given its id
        """
        character = CharacterSheet.objects.get(id=identifier)

        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('description')
        parser.add_argument('hit_points')
        parser.add_argument('level')
        parser.add_argument('experience')
        parser.add_argument('strength')
        parser.add_argument('desterity')
        parser.add_argument('costitution')
        parser.add_argument('intelligence')
        parser.add_argument('wisdom')
        parser.add_argument('charisma')
        parser.add_argument('race')
        parser.add_argument('klass')
        parser.add_argument('items', action='append') 
        parser.add_argument('owner')
        parse_result = parser.parse_args(req=self.request)
    
        no_docs_updated = character.update(**parse_result)

        if no_docs_updated == 1:  # the row was updated successfully
            character = CharacterSheet.objects.get(id=identifier)
            return loads(character.to_json())

    @staticmethod
    def delete(identifier):
        """
        Deletes a character given its id
        """
        target = CharacterSheet.objects.get(id=identifier)
        target_data = loads(target.to_json())

        target.delete()

        return target_data

    @staticmethod
    def new_memento(identifier):


        character_sheet = CharacterSheet.objects.get(id=identifier) 
        memento = ConcreteCharacterMemento()
        
        memento.hit_points = character_sheet.hit_points
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
    