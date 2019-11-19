import mongoengine

from flask import Flask
from flask_restplus import Api
from views import campaign_api, match_api, event_api, rule_api, character_api, damage_api

app = Flask(__name__)
api = Api(app = app, 
		  version = "1.0", 
		  title = "MoP - Campaigns service", 
		  description = "Campaigns service API")

if __name__ == '__main__':
    mongoengine.connect(db='mop', host='mongodb://mongo_main:27017/mop',
                        alias='campaigns_connection')

    api.add_namespace(campaign_api.api)
    api.add_namespace(event_api.api)
    api.add_namespace(match_api.api)
    api.add_namespace(rule_api.api)
    api.add_namespace(character_api.api)
    api.add_namespace(damage_api.api)
    
    app.run(host='0.0.0.0', port=5001, debug=True)
