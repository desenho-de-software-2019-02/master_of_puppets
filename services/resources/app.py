from flask import Flask
import mongoengine

from flask_restplus import Api
from views import character_api, item_api, dice_api

app = Flask(__name__)
api = Api(app)

mongoengine.connect('mop', host='mongo:27017')

if __name__ == '__main__':
    api.add_namespace(character_api.api)
    api.add_namespace(item_api.api)
    api.add_namespace(dice_api.api)
    app.run(host='0.0.0.0', port=5000, debug=True)
