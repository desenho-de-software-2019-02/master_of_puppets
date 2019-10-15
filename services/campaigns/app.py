from flask import Flask

from flask_restplus import Api
from views import campaign_api, match_api, event_api

app = Flask(__name__)
api = Api(app)

if __name__ == '__main__':
    api.add_namespace(campaign_api.api)
    api.add_namespace(event_api.api)
    api.add_namespace(match_api.api)
    
    app.run(host='0.0.0.0', port=5001)




