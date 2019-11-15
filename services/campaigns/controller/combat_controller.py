import abc
import mongoengine

from models.combat import CombatManager
from models.combat import Turn
from models.combat import CharacterTurn
from models.character import Character

from json import dumps, loads
from flask_restplus import reqparse

mongoengine.connect(db='mop', host='mongodb://mongo_main:27017/mop',
                    alias='campaigns_connection')


class CombatManagerController(object):
    def __init__(self, request):
        self.request = request

    def new(self):
        parser = reqparse.RequestParser()
        parser.add_argument('players', action='append')
        parse_result = parser.parse_args(req=self.request)
 
        print("parse_result")
        players = parse_result['players']
        l = []
        
        for player in players:
            turn = CharacterTurn()
            turn.character = player
            turn.save()
            l.append(turn)
        
        combat_manager = CombatManager()
        combat_manager.turn_list = l
        combat_manager.active_turn = l.first()
        combat_manager.save()

        return combat_manager

    def list_players(self, identifier):
        target = CombatManager.objects.get(id=identifier)
        l = []
        
        for turn in target.turn_list:
            t = CharacterTurn.objects.get(id=turn.id)
            if(t != []):
                l.append(str(t.character.id))

        return l

    def active_turn(self, identifier):
        """
        Returns the character that owns the turn
        """
        target = CombatManager.objects.get(id=identifier)
        turn = Turn.objects.get(id=target.active_turn.id)
        character = Character.objects.get(id=turn.character.id)
        return loads(character.to_json())

    def reorder(self):
        pass

    def add_player(self):
        pass

    def next_turn(self):
        pass

    def remove_player(self):
        pass



class TurnController():
    class Meta:
        abstract = True

    # @abstractmethod
    def init_turn(self):
        pass

    # @abstractmethod
    def create_turn(self):
        pass

    # @abstractmethod
    def end_turn(self):
        pass



class classname(object):
    pass
