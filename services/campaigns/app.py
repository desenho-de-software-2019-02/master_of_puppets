import mongoengine

from flask import Flask
from flask_restplus import Api

from views import campaign_api
from views import match_api
from views import event_api
from views import rule_api
from views import character_api

app = Flask(__name__)
api = Api(app)

if __name__ == '__main__':
    mongoengine.connect(db='mop', host='mongodb://mongo_main:27017/mop',
                        alias='campaigns_connection')
    # mongoengine.connect('')

    api.add_namespace(campaign_api.api)
    api.add_namespace(event_api.api)
    api.add_namespace(match_api.api)
    api.add_namespace(rule_api.api)
    api.add_namespace(character_api.api)

    app.run(host='0.0.0.0', port=5001)
