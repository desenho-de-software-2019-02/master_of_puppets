from flask import Flask

from flask_restplus import Api
from views import character_api, classes_view

app = Flask(__name__)
#api = Api(app)
api = Api(app = app, 
		  version = "1.0", 
		  title = "Master of Puppets API", 
		  description = "Manage cruds of the application")

if __name__ == '__main__':
    api.add_namespace(character_api.api)
    api.add_namespace(classes_view.api)
    app.run(host='0.0.0.0', port=5000, debug=True)




