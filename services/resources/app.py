from flask import Flask
import mongoengine
import mongoengine.fields as fields
from flask_restplus import Api
from views import character_api, item_api, dice_api, class_api

app = Flask(__name__)
api = Api(app = app, 
		  version = "1.0", 
		  title = "Master of Puppets API", 
		  description = "Manage cruds of the application")

if __name__ == '__main__':

    mongoengine.connect('mop', host='mongo:27017')

    api.add_namespace(character_api.api)
    api.add_namespace(item_api.api)
    api.add_namespace(dice_api.api)
    api.add_namespace(class_api.api)
    app.run(host='0.0.0.0', port=5000, debug=True)
