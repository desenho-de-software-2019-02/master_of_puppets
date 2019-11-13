import json
from flask_restplus import Namespace, Resource, fields
from flask import request
import requests
import logging

api = Namespace('damage', description='damage')
RESOURCES_URL = 'http://webserver/api/resources/'

class DamageController:
    def __init__(self, request):
        self.request = request.get_json()
        self.define_strategy()

    def define_strategy(self):
        logging.warning(self.request)
        if(self.request.get('skill') is not None):
            self._strategy = SkillStrategy(self.request)
        elif(self.request.get('item') is not None):
            self._strategy = ItemStrategy()
        else:
            self._strategy = BasicAttackStrategy()
    def trial(self):
        self._strategy.trial()


class DamageAction: 
    def trial(self):
        pass

class SkillStrategy(DamageAction):
    def __init__(self, request):
        self.request = request
    def trial(self):
        logging.warning("Skill Strategy")
        self._get()
    def _get(self):
        skill = requests.get(url='{}/skills/{}'.format(RESOURCES_URL, self.request['skill']), timeout=5)
        logging.warning(skill.text)

class BasicAttackStrategy(DamageAction):
    def trial(self):
        logging.warning("Basic Attack Strategy")

class ItemStrategy(DamageAction):
    def trial(self):
        logging.warning("Item Attack Strategy")