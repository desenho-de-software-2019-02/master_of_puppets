import unittest 
import simplejson as json
import requests

base_json = {
  "name": "anao",
  "description": "blz",
  "effects": [
    "string"
  ],
  "restrictions": [
    "string"
  ],
  "exclusive_skills": [
    "string"
  ]
}

def get(id='', port=9001, endpoint='races'):
    base_url = "http://0.0.0.0:{}/{}/{}".format(port, endpoint, id)
    headers = { 'accept': 'application/json', 'Content-Type' : 'application/json' }
    r = requests.get(base_url, headers=headers)
    return r

def post(data, id='', port=9001, endpoint='races'):
    base_url = "http://0.0.0.0:{}/{}/{}".format(port, endpoint, id)
    headers = { 'accept': 'application/json', 'Content-Type' : 'application/json' }
    r = requests.post(base_url, data=json.dumps(data), headers=headers)
    return r
    
def put(data, id='', port=9001, endpoint='races'):
    base_url = "http://0.0.0.0:{}/{}/{}".format(port, endpoint, id)
    headers = { 'accept': 'application/json', 'Content-Type' : 'application/json' }
    r = requests.put(base_url, data=json.dumps(data), headers=headers)
    return r
   
def delete(id='', port=9001, endpoint='races'):
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
        data['description'] = 'n blz'
        
        put(id=id, data=data)
        
        out_description = json.loads(get(id=id)._content)

        self.assertEqual(data['description'], out_description['description'])

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
