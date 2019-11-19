import unittest 
import simplejson as json
import requests

def get(id='', port=9001, endpoint='dice'):
    base_url = "http://0.0.0.0:{}/{}/{}".format(port, endpoint, id)
    headers = { 'accept': 'application/json', 'Content-Type' : 'application/json' }
    r = requests.get(base_url, headers=headers)
    return r


       
class TestCampaignMethods(unittest.TestCase): 
    def setUp(self): 
        pass
        
    def test_get_id(self):
        id = '3d8'
        out = get(id=id)
        
        self.assertEqual(out.status_code, 200)
  
if __name__ == '__main__': 
    unittest.main() 
