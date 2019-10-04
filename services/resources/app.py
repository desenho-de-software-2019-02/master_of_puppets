from flask import Flask

from flask_restplus import Api
from views import character_api
from views import race_api

app = Flask(__name__)
api = Api(app)

if __name__ == '__main__':
    api.add_namespace(character_api.api)
    api.add_namespace(race_api.api)
    app.run(host='0.0.0.0', port=5000, debug=True)



