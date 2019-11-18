import unittest 
import simplejson as json
import requests
from test_campaign.test_match import get_random_id as get_match_id
from test_campaign.test_campaign import get_random_id as get_campaign_id
import os

base_json = {
  "players": [
    "joao", "marcelo"
  ]
}

user_json = {"email":"dedao@dev.com","password":"qwertyuiop"}
headers = { 'accept': 'application/json', 'Content-Type' : 'application/json' }


def patch(id='', port='9000', endpoint='matches/combat', page='change-turn/'):
    append = '/'.join(list(filter(None, [port, endpoint, id, page])))
    base_url = "http://0.0.0.0:{}".format(append)
    r = requests.patch(base_url, headers=headers)
    return r

def get(id='', port='9000', endpoint='matches/combat', page=''):
    append = '/'.join(list(filter(None, [port, endpoint, id, page])))
    base_url = "http://0.0.0.0:{}".format(append)
    r = requests.get(base_url, headers=headers)
    return r

def post(data, id='', port='9000', endpoint='matches/combat', page=''):
    append = '/'.join(list(filter(None, [port, endpoint, id, page])))
    base_url = "http://0.0.0.0:{}".format(append)
    r = requests.post(base_url, data=json.dumps(data), headers=headers)
    return r
    
def get_random_id():
    out = post(data=base_json, endpoint="matches", id=match_id, page="combat/")
    combat_id = json.loads(out._content)['battles'][-1]['$oid']

    return combat_id
       
match_id = get_match_id()
user_name = json.loads(requests.post("http://0.0.0.0:3030/auth/login", data=json.dumps(user_json), headers=headers)._content)['username']
character_sheet = {
  "name": "string",
  "description": "string",
  "hit_points": 0,
  "level": 0,
  "experience": 0,
  "strength": 0,
  "dexterity": 0,
  "constitution": 0,
  "intelligence": 0,
  "armor_class": 0,
  "fortitude": 0,
  "reflex": 0,
  "will": 0,
  "wisdom": 0,
  "charisma": 0,
  "character_class": "string",
  "race": "string",
  "items": [
    "string"
  ],
  "skills": [
    "string"
  ],
  "owner": user_name
}

def get_cs_id():
    post(data=character_sheet, port='9001', endpoint='character_sheet/')
    out = json.loads(get(port='9001', endpoint='character_sheet/')._content)
    id = out[-1]['_id']['$oid']

    return id

cs_id = get_cs_id()

campaign_id = get_campaign_id()
character = {
  "user": user_name,
  "character_sheet": cs_id,
  "campaign": campaign_id
}

def get_character_id():
    post(data=character, endpoint='characters/')
    out = json.loads(get(endpoint='characters/')._content)
    
    id = out[-1]['_id']['$oid']

    return id

char_id = get_character_id()
base_json['players'] = [char_id]
combat_id = ''

class TestCampaignMethods(unittest.TestCase): 
    def setUp(self):
        pass
    
    def test_get_players(self):
        id = get_random_id()
        out = get(id=id, page='players/')
        
        self.assertEqual(out.status_code, 200)
        
    def test_get_current_turn(self):
        id = get_random_id()
        out = get(id=id, page='current-turn/')
        
        self.assertEqual(out.status_code, 200)

    def test_post_new_player_to_combat(self):
        campaign_id = get_campaign_id()
        character['campaign'] = campaign_id
        char_id = get_character_id()
        base_json['players'].append(char_id)
        id = get_random_id()
        
        
        out = post(data=base_json, id=id, page='players/')
        
        self.assertEqual(out.status_code, 200)

    def test_post_new_combat(self):
        out = post(data=base_json, endpoint="matches", id=match_id, page="combat/")
        combat_id = json.loads(out._content)['battles'][-1]['$oid']
        self.assertEqual(out.status_code, 200)

    def test_patch_change_turn(self):
        id = get_random_id()
        out = patch(id=id)
        self.assertEqual(out.status_code, 200)
    
  
if __name__ == '__main__': 
    unittest.main() 
