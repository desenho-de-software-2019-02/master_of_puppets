import abc
import mongoengine

from models.battle import CombatManager
from models.battle import Turn
from models.battle import CharacterTurn
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
            print(player)
            turn = CharacterTurn(player).save()
            l.append(turn)
        
        combat_manager = CombatManager(l)
        combat_manager.save()
        print("*"*1000 )
        print(combat_manager.__dict__)
        return combat_manager

    def list_players(self, identifier):
        print('*'*100 )
        print(identifier)
        target = CombatManager.objects.get(id=identifier)
        l = []
        for turn in target.turns:
            t = CharacterTurn.objects.get(id=turn)
            if(t != []):
                l.append(t.character)

        return l
        

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
