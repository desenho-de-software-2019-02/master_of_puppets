from flask_restplus import Namespace
import requests
import logging
import json
from views import character_api
from models import event
from datetime import datetime

RESOURCES_URL = 'http://webserver/api/resources'

class DamageController:
    def __init__(self, request):
        self.request = request.get_json()

    def calculate(self):
        log_handler = LogHandler(None)
        if self.request.get('step') == 1:
            threshold_handler = ThresholdHandler(log_handler)
            action_handler = ActionHandler(threshold_handler)
            resource_handler = ResourcesHandler(action_handler)
        elif self.request.get('step') == 2:
            deal_handler = DealHandler(log_handler)
            resource_handler = ResourcesHandler(deal_handler)

        req = Object()
        req.request = self.request
        response = resource_handler.handle_request(req)
        return response.result

# Chain of Responsibility links implementation
class Handler:
    def  __init__(self, sucessor):
        self._sucessor = sucessor
    
    def handle_request(self, obj):
        if self._sucessor:
            return self._sucessor.handle_request(obj)
        else:
            return obj


class ResourcesHandler(Handler):
    def handle_request(self, obj):
        obj.caster = self._get_character_sheet(obj.request.get('caster'))
        obj.target = self._get_character_sheet(obj.request.get('target'))
        return super().handle_request(obj)

    def _get_character_sheet(self, character_id):
        character = character_api.CharacterDetail.get(self, character_id)
        character_sheet = requests.get(url='{}/character_sheet/{}'.format(RESOURCES_URL,character.get('character_sheet')))
        return character_sheet.json()


class ActionHandler(Handler):
    def handle_request(self, obj):
        self._define_strategy(obj)
        obj = self._strategy.load(obj)
        return super().handle_request(obj)

    def _define_strategy(self, obj):
        if(obj.request.get('skill') is not None):
            self._strategy = SkillStrategy(obj.request)
        elif(obj.request.get('item') is not None):
            self._strategy = ItemStrategy(obj.request)
        else:
            self._strategy = BasicAttackStrategy(obj.request)


class DealHandler(Handler):
    def handle_request(self, obj):
        obj.target['hit_points']  = obj.target.get('hit_points') - obj.request.get('dice_result')
        target_id = obj.target.pop('_id')
        requests.put(url='{}/character_sheet/{}'.format(RESOURCES_URL,
                            target_id.get('$oid')), data=obj.target).json()
        return super().handle_request(obj)

class ThresholdHandler(Handler):
    def handle_request(self, obj):
        if(obj.request.get('dice_result') == 20):
            obj.result = { 'critical_strike': True, 'succeeded': True}
        elif(obj.request.get('dice_result') >= obj.threshold):
            obj.result = { 'critical_strike': False, 'succeeded': True}
        else:
            obj.result = {'critical_strike': False, 'succeeded': False}
        return super().handle_request(obj)

# CHANGE WHEN MERGED WITH LOG/EVENT SYSTEM
class LogHandler(Handler):
    def handle_request(self, obj):
        if(obj.request.get('step') == 1):
            message = (
            f"Player {obj.caster.get('name')} attacked Player {obj.target.get('name')} "
            f"with {obj.attack_component['name'] if hasattr(obj,'attack_component') else 'with a basic attack.'}."
            f" The attack {'was sucessful.' if obj.result['succeeded'] else 'failed miserably.'}"
            f"{' It was a critical strike' if obj.result['critical_strike'] else ''}"
            )
        elif(obj.request.get('step') == 2):
            message = (
            f"Player {obj.target.get('name')} suffered {obj.request.get('dice_result')} damage."
            f" {obj.target.get('name')} has now {obj.target.get('hit_points')} hp"
            )
        obj.result['message'] = message
        time = datetime.utcnow()
        request =   {
            "event_type": "Damage Action",
            "description": obj.result['message'],
            "event_date": time,
            "data": "request: {}, result: {}".format(obj.request, obj.result)
            }
        event_response = event.Event.from_json(json.dumps(request,sort_keys=True, default=str)).save()

        return super().handle_request(obj)


class DamageAction:
    def __init__(self, request):
        self.request = request

    def load(self):
        pass


class SkillStrategy(DamageAction):
    def load(self, obj):
        obj.attack_component = self._get_skill(obj)
        obj.threshold = obj.caster.get(obj.attack_component.get('attack_multiplier')) -\
                    obj.target.get(obj.attack_component.get('defense_multiplier')) +\
                    obj.attack_component.get('attack_bonus')
        return obj

    def _get_skill(self, obj):
        logging.warning(requests.get(url='{}/skills/{}'.format(RESOURCES_URL,
                            obj.request['skill'])).json())
        return requests.get(url='{}/skills/{}'.format(RESOURCES_URL,
                            obj.request['skill'])).json()


class BasicAttackStrategy(DamageAction):
    def load(self, obj):
        obj.threshold = obj.caster.get('strength') -\
                    obj.target.get('armor_class')
        return obj


class ItemStrategy(DamageAction):
    def load(self, obj):
        self.attack_component = self._get_item(obj)
        obj.threshold = obj.caster.get('strength') -\
                    obj.target.get('armor_class') +\
                    obj.attack_component.get('proficiency')
        return obj

    def _get_item(self):
        return requests.get(url='{}/items/{}'.format(RESOURCES_URL,
                            obj.request['item'])).json()


class Object(object):
    pass