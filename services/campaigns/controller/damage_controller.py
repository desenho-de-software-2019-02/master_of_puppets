import json
from flask_restplus import Namespace, Resource, fields
from flask import request
import requests
import logging
from views import character_api

api = Namespace('damage', description='damage')

RESOURCES_URL = 'http://webserver/api/resources'

class DamageController:
    def __init__(self, request):
        self.request = request.get_json()
        self.define_strategy()

    def define_strategy(self):
        if(self.request.get('skill') is not None):
            self._strategy = SkillStrategy(self.request)
        elif(self.request.get('item') is not None):
            self._strategy = ItemStrategy(self.request)
        else:
            self._strategy = BasicAttackStrategy()

    def calculate(self):
        if(self.request.get('dice_result') == 20):
            return { 'critical_strike': True, 'succeeded': True }
        else:
            return self._strategy.trial()


class DamageAction:
    def __init__(self, request):
        self.request = request
        self.caster = self._get_character_sheet(self.request.get('caster'))
        self.target = self._get_character_sheet(self.request.get('target'))


    def trial(self):
        pass

    def _get_character_sheet(self, character_id):
        character = character_api.CharacterDetail.get(self, character_id)
        character_sheet = requests.get(url='{}/character_sheet/{}'.format(RESOURCES_URL,character.get('character_sheet')))
        return character_sheet.json()

    def validate_threshold(self, threshold):
        if(self.request.get('dice_result') >= threshold):
            return { 'critical_strike': False, 'succeeded': True}
        else:
            return { 'critical_strike': False, 'succeeded': False}


class SkillStrategy(DamageAction):
    def trial(self):
        self.skill = self._get_skill()
        threshold = self.caster.get(self.skill.get('attack_multiplier')) -\
                    self.target.get(self.skill.get('defense_multiplier')) +\
                    self.skill.get('attack_bonus')
        return self.validate_threshold(threshold)
    
    def _get_skill(self):
        return requests.get(url='{}/skills/{}'.format(RESOURCES_URL,
                            self.request['skill'])).json()


class BasicAttackStrategy(DamageAction):
    def trial(self):
        logging.warning("Basic Attack Strategy")

class ItemStrategy(DamageAction):
    def trial(self):
        self.item = self._get_item()
        threshold = self.caster.get('strength') -\
                    self.target.get('costitution') 
                    # AFTER ADDED PROFICIENCY TO ITEM
                    # + self.item.get('proficiency')
        return self.validate_threshold(threshold)

    def _get_item(self):
        return requests.get(url='{}/items/{}'.format(RESOURCES_URL,
                            self.request['item'])).json()