from flask import Flask
import mongoengine

from flask_restplus import Api
from views import character_sheet_api
from views import item_api
from views import dice_api
from views import race_api
from views import skill_api


app = Flask(__name__)
api = Api(app)

# mongoengine.disconnect()
# mongoengine.connect('dev', host='mongodb://root:root@localhost:27017/mop')

if __name__ == '__main__':

    mongoengine.connect('mop', host='mongo:27017')

    """
    Import your api namespaces below. Remember to import them.
    """
    api.add_namespace(character_sheet_api.api)
    api.add_namespace(race_api.api)
    api.add_namespace(item_api.api)
    api.add_namespace(dice_api.api)
    api.add_namespace(skill_api.api)
    
    app.run(host='0.0.0.0', port=5000, debug=True)
