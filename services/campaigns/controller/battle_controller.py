import abc
import mongoengine

from models.battle import CombatManager
from models.battle import Turn
from models.battle import CharacterTurn

mongoengine.connect(db='mop', host='mongodb://mongo_main:27017/mop',
                    alias='campaigns_connection')


class CombatManagerController(object):
    def __init__(self, request):
        self.request = request

    def create(self):
        players = [
            '5dc41dab60ba5e891862e005',
            '5dc41dab60ba5e891861e005',
            '5dc41dab60ba5e891864e005',
        ]
        
        l = []
        
        for player in players:
            print(player)
            turn = CharacterTurn(player).save()
            l.append(turn)
        
        combat_manager = CombatManager(l)
        combat_manager.save()

        

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
