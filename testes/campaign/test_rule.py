import unittest 
import simplejson as json
import requests

base_json = {
  "name": "regra de ouro",
  "description": "n vale X",
  "character_classes": [
  ],
  "races": [
  ],
  "items": [
  ],
  "skills": [
  ]
}

def get(id='', port=9000, endpoint='rules'):
    base_url = "http://0.0.0.0:{}/{}/{}".format(port, endpoint, id)
    headers = { 'accept': 'application/json', 'Content-Type' : 'application/json' }
    r = requests.get(base_url, headers=headers)
    return r

def post(data, id='', port=9000, endpoint='rules'):
    base_url = "http://0.0.0.0:{}/{}/{}".format(port, endpoint, id)
    headers = { 'accept': 'application/json', 'Content-Type' : 'application/json' }
    r = requests.post(base_url, data=json.dumps(data), headers=headers)
    return r
    
def put(data, id='', port=9000, endpoint='rules'):
    base_url = "http://0.0.0.0:{}/{}/{}".format(port, endpoint, id)
    headers = { 'accept': 'application/json', 'Content-Type' : 'application/json' }
    r = requests.put(base_url, data=json.dumps(data), headers=headers)
    return r
   
def delete(id='', port=9000, endpoint='rules'):
    base_url = "http://0.0.0.0:{}/{}/{}".format(port, endpoint, id)
    headers = { 'accept': 'application/json' }
    r = requests.delete(base_url, headers=headers)
    return r

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
        data = base_json
        data['name'] = 'regra de prata'
        
        put(id=id, data=data)
        
        out_name = json.loads(get(id=id)._content)

        self.assertEqual(data['name'], out_name['name'])

    def test_delete(self):
        id = get_random_id()
        out = delete(id=id)

        print('id do delete = '+id)
        self.assertEqual(out.status_code, 200)
    
    def test_get_id(self):
        id = get_random_id()
        out = get(id=id)
        
        self.assertEqual(out.status_code, 200)
  
if __name__ == '__main__': 
    unittest.main() 
