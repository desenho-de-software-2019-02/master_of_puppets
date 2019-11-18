import unittest 
import simplejson as json
import requests
from test_campaign.test_campaign import get_random_id as get_campaign_id


user_json = {"email":"dedao@dev.com","password":"qwertyuiop"}
headers = { 'accept': 'application/json', 'Content-Type' : 'application/json' }


def patch(id='', port='9000', endpoint='characters/', page=''):
    append = '/'.join(list(filter(None, [port, endpoint, id, page])))
    base_url = ("http://0.0.0.0:{}".format(append)).replace('characters//', 'characters/')

    r = requests.patch(base_url, headers=headers)
    return r

def get(id='', port='9000', endpoint='characters/', page=''):
    append = '/'.join(list(filter(None, [port, endpoint, id, page])))
    base_url = ("http://0.0.0.0:{}".format(append)).replace('characters//', 'characters/')

    r = requests.get(base_url, headers=headers)
    return r

def post(data, id='', port='9000', endpoint='characters/', page=''):
    append = '/'.join(list(filter(None, [port, endpoint, id, page])))
    base_url = ("http://0.0.0.0:{}".format(append)).replace('characters//', 'characters/')

    r = requests.post(base_url, data=json.dumps(data), headers=headers)
    return r

def put(data, id='', port='9000', endpoint='characters/', page=''):
    append = '/'.join(list(filter(None, [port, endpoint, id, page])))
    base_url = ("http://0.0.0.0:{}".format(append)).replace('characters//', 'characters/')

    r = requests.put(base_url, data=json.dumps(data), headers=headers)
    return r
   
def delete(id='', port='9000', endpoint='characters/', page=''):
    append = '/'.join(list(filter(None, [port, endpoint, id, page])))
    base_url = ("http://0.0.0.0:{}".format(append)).replace('characters//', 'characters/')

    r = requests.delete(base_url, headers=headers)
    return r
       
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
    post(data=character_sheet, port='9001', endpoint='character_sheet')
    out = json.loads(get(port='9001', endpoint='character_sheet')._content)
    id = out[-1]['_id']['$oid']

    return id

cs_id = get_cs_id()

campaign_id = get_campaign_id()
base_json = {
  "user": user_name,
  "character_sheet": cs_id,
  "campaign": campaign_id
}

def get_character_id():
    post(data=base_json)
    out = json.loads(get()._content)
    id = out[-1]['_id']['$oid']

    return id

char_id = get_character_id()

def get_random_id():
    post(base_json)
    out = json.loads(get()._content)
    id = out[-1]['_id']['$oid']

    return id
       
class TestCampaignMethods(unittest.TestCase): 
    def setUp(self): 
        pass
    
    def test_get(self):
        out = get()
        
        self.assertEqual(out.status_code, 200)
        
    def test_post(self):
        out = post(base_json)
        
        self.assertEqual(out.status_code, 200)

    def test_put(self):
        id = get_random_id()
        campaign_id = get_campaign_id()
        data = base_json
        data['campaign'] = campaign_id
        
        aut = put(id=id, data=data)
        out = get(id=id)._content
        out_campaign = json.loads(out)

        self.assertEqual(data['campaign'], out_campaign['campaign']['$oid'])

    def test_delete(self):
        id = get_random_id()
        out = delete(id=id)

        self.assertEqual(out.status_code, 200)
    
    def test_get_id(self):
        id = get_random_id()
        out = get(id=id)
        
        self.assertEqual(out.status_code, 200)
  
if __name__ == '__main__': 
    unittest.main() 
