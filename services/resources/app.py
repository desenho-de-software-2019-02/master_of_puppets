from flask import Flask
import mongoengine
from flask_restplus import Api

from views import character_sheet_api
from views import item_api
from views import dice_api
from views import race_api
from views import character_class_api
from views import skill_api

app = Flask(__name__)
<<<<<<< HEAD
api = Api(app = app,
		  version = "1.0",
		  title = "Master of Puppets API",
		  description = "Manage cruds of the application")

# mongoengine.disconnect()
# mongoengine.connect('dev', host='mongodb://root:root@localhost:27017/mop')
=======
api = Api(app = app, 
		  version = "1.0", 
		  title = "MoP - Resources service", 
		  description = "Resources service API")
>>>>>>> 5e339a62f04235470b5e23f21c5e56a723c6085c

if __name__ == '__main__':
    mongoengine.connect('mop', host='mongo:27017')

    """
    Import your api namespaces below. Remember to import them.
    """
    api.add_namespace(character_sheet_api.api)
    api.add_namespace(race_api.api)
    api.add_namespace(item_api.api)
    api.add_namespace(dice_api.api)
    api.add_namespace(character_class_api.api)

    api.add_namespace(skill_api.api)

    app.run(host='0.0.0.0', port=5000, debug=True)
