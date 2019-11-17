import os
import mongoengine
import requests as req

from models.combat import CombatManager
from models.combat import Turn
from models.combat import CharacterTurn
from models.character import Character

from json import loads
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

        players = parse_result['players']
        turn_list = []
        turn_controller = TurnController()

        for player in players:
            turn = turn_controller.create_turn(player)
            dice_res = self.__get_action_d20()
            turn_list.append([turn, dice_res['result']])

        self.__sort_by_initiative(turn_list)

        combat_manager = CombatManager()
        combat_manager.turn_list = []

        combat_manager.turn_list = list(map(lambda tup: tup[0], turn_list))

        combat_manager.active_turn = 0
        combat_manager.save()

        a = self.active_turn(combat_manager.id)
        turn_controller.init_turn(a)

        return combat_manager

    def list(self):
        return CombatManager.objects.all()

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
        turn = Turn.objects.get(id=target.turn_list[target.active_turn].id)
        return turn

    def active_turn_owner(self, identifier):
        turn = self.active_turn(identifier)
        character = Character.objects.get(id=turn.character.id)
        return loads(character.to_json())

    @staticmethod
    def __sort_by_initiative(turns_list):
        print(turns_list)
        turns_list.sort(key=lambda player_tup: player_tup[1], reverse=True)
        

    def add_player(self, identifier):
        parser = reqparse.RequestParser()
        parser.add_argument('players', action='append')
        parse_result = parser.parse_args(req=self.request)
        players = parse_result['players']

        combat_manager = CombatManager.objects.get(id=identifier)
        a_place_to_belong = combat_manager.active_turn + 1

        for player in players:
            turn = CharacterTurn()
            turn.character = player
            turn.save()
            combat_manager.turn_list.insert(a_place_to_belong, turn)
        combat_manager.save()

        return loads(combat_manager.to_json())

    def next_turn(self, identifier):
        combat_manager = CombatManager.objects.get(id=identifier)
        turn_controller = TurnController()

        actual = self.active_turn(identifier)
        turn_controller.end_turn(actual)

        combat_manager.active_turn = (
            combat_manager.active_turn + 1) % len(combat_manager.turn_list)
        combat_manager.save()

        new_active_turn = self.active_turn(identifier)
        turn_controller.init_turn(new_active_turn)

        return self.active_turn_owner(identifier)

    def remove_player(self):
        pass

    @staticmethod
    def __get_action_d20():
        a = req.get('http://%s/dice/1d20' % os.environ.get('RESOURCES_URL'))
        
        return loads(a.text)


class TurnController():
    class Meta:
        abstract = True

    @staticmethod
    def create_turn(player):
        """
        TurnController.create_turn
        """
        turn = CharacterTurn()
        turn.character = player
        turn.save()
        
        return turn

    @staticmethod
    def init_turn(turn):
        """
        Inits turn and calls log. Dumbass
        """
        pass

    @staticmethod
    def end_turn(turn):
        """
        Ends turn and calls log
        """
        pass

    def list(self):
        """
        Lists all turns
        """
        return Turn.objects.all()
