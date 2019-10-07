from flask_restplus import Namespace, Resource, Api, fields
from core import race_controller
from flask import request, jsonify,Flask
flask_app = Flask(__name__)

app = Api(app = flask_app, 
		  version = "1.0", 
		  title = "Name Recorder", 
		  description = "Manage names of various users of the application")
#api = Namespace('Race', description='class relacionada a raça ')
api = app.namespace('race', description='CRUD Race')

# declaraçao dos tipos de dados aceitos pelo metodo post
create = api.model('create', {
    "name":fields.String(),
    "description":fields.String(),
    "restriction": fields.List(fields.String),
    "exclusiveSkills": fields.List(fields.String)
})

delete = api.model('delete', {
    "name":fields.String(),
})

update = api.model('update', {
    "old_name":fields.String(),
    "name":fields.String(),
    "description":fields.String(),
    "restriction": fields.List(fields.String),
    "exclusiveSkills": fields.List(fields.String)
})


  


@api.route("/create")

class raceCreate(Resource):
    @api.expect([create])
    def post(self):
        data = request.get_json()
        result = race_controller.create_race(data)
        return result;




@api.route('/read')
class raceRead(Resource):
    def get(self):
        return race_controller.get_race()

@api.route('/delete')
class raceDelete(Resource):
    @api.expect([delete])
    def post(self):
        data = request.get_json()
        result =  race_controller.delete_race(data)
        return result

@api.route('/update')
class raceUpdate(Resource):
    @api.expect([update])
    def post(self):
        data = request.get_json()
        result = race_controller.update_race(data)
        return result;  
