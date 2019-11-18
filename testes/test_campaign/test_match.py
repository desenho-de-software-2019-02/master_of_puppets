import unittest 
import simplejson as json
import requests

from test_campaign.test_campaign import get_random_id as get_campaign_id
from test_campaign.test_events import get_random_id as get_events_id

from mongoengine import *
from bson.objectid import ObjectId
base_json = {
  "name": "episodio 21",
  "events": [
    "string"
  ],
  "description": "pessoa X aparece",
  "campaign": "string",
}

def get(id='', port=9000, endpoint='matches'):
    base_url = "http://0.0.0.0:{}/{}/{}".format(port, endpoint, id)
    headers = { 'accept': 'application/json', 'Content-Type' : 'application/json' }
    r = requests.get(base_url, headers=headers)
    return r

def post(data, id='', port=9000, endpoint='matches'):
    base_url = "http://0.0.0.0:{}/{}/{}".format(port, endpoint, id)
    headers = { 'accept': 'application/json', 'Content-Type' : 'application/json' }
    r = requests.post(base_url, data=json.dumps(data), headers=headers)
    return r
    
def put(data, id='', port=9000, endpoint='matches'):
    base_url = "http://0.0.0.0:{}/{}/{}".format(port, endpoint, id)
    headers = { 'accept': 'application/json', 'Content-Type' : 'application/json' }
    r = requests.put(base_url, data=json.dumps(data), headers=headers)
    return r
   
def delete(id='', port=9000, endpoint='matches'):
    base_url = "http://0.0.0.0:{}/{}/{}".format(port, endpoint, id)
    headers = { 'accept': 'application/json' }
    r = requests.delete(base_url, headers=headers)
    return r

def get_random_id():
    post(base_json)
    out = get()
    id = json.loads(out._content)[-1]['_id']['$oid']
    return id
       
class TestCampaignMethods(unittest.TestCase): 
    def setUp(self): 
        campaign_id = get_campaign_id()
        event_id = get_events_id()
        base_json['events'] = [event_id]
        base_json['campaign'] = campaign_id
        pass

    def test_put(self):
        id = get_random_id()
        data = base_json

        data['description'] = 'Y aparece'
        
        
        put(id=id, data=data)
        
        out_description = json.loads(get(id=id)._content)

        self.assertEqual(data['description'], out_description['description'])

if __name__ == '__main__': 
    unittest.main() 
