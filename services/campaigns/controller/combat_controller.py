import abc
import os
import mongoengine
import requests as req

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

        players = parse_result['players']
        l = []

        for player in players:
            turn = CharacterTurn()
            turn.character = player
            turn.save()
            dice_res = self.__get_action_d20()
            l.append([turn, dice_res])

        l = self.__reorder(l)

        combat_manager = CombatManager()
        combat_manager.turn_list = []

        for elem in l:
            combat_manager.turn_list.append(elem[0])

        combat_manager.active_turn = 0
        combat_manager.save()

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
        character = Character.objects.get(id=turn.character.id)
        return loads(character.to_json())

    def __reorder(self, turns_list) -> list:
        return self.__sort(turns_list)

    @staticmethod
    def __sort(listt):
        for i in range(0, listt.__len__() - 1):
            for j in range(0, listt.__len__() - (i + 1)):
                if listt[j][1]['result'] < listt[j + 1][1]['result']:
                    listt[j + 1], listt[j] = listt[j], listt[j + 1]
        return listt

    def add_player(self, identifier):
        parser = reqparse.RequestParser()
        parser.add_argument('players', action='append')
        parse_result = parser.parse_args(req=self.request)
        players = parse_result['players']

        combat_manager = CombatManager.objects.get(id=identifier)
        a_place_to_belong = combat_manager.active_turn

        for player in players:
            print(repr(player))
            combat_manager.turn_list.insert(a_place_to_belong, player)
        
        print((combat_manager.__dict__))
        combat_manager.save()
        return loads(combat_manager.to_json())

    def next_turn(self):
        # combat_manager = CombatManager.objects.get(id=identifier)
        # combat_manager.active_turn = (
        #     combat_manager.active_turn + 1) % len(combat_manager.turn_list)

        # combat_manager.save()

        # return loads(combat_manager.to_json())
        pass

    def remove_player(self):
        pass

    @staticmethod
    def __get_action_d20():
        a = req.get('http://%s/dice/1d20' % os.environ.get('RESOURCES_URL'))
        return loads(a.text)


class TurnController():
    class Meta:
        abstract = True

    def init_turn(self):
        pass

    def create_turn(self):
        pass

    def end_turn(self):
        pass

    def list(self):
        return Turn.objects.all()
