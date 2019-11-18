from json import dumps, loads
from models.match import Match
from controller.combat_controller import CombatManagerController
from base.controller import BaseController
from flask_restplus import reqparse

class MatchController(BaseController):

    def set_edit_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name')
        self.parser.add_argument('events', action='append')
        self.parser.add_argument('description')
        self.parser.add_argument('campaign')
 
        return self.parser
    
    def start_battle(self, identifier):
    
        controller = CombatManagerController(self.request)
        battle_id = controller.new()

        target = Match.objects.get(id=identifier)
        target.update(push__battles=battle_id)
        target = Match.objects.get(id=identifier)

        return(loads(target.to_json()))
