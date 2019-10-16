from flask_restplus import Namespace, Resource, Api, fields
from core.race_controller import raceController
from flask import request, jsonify,Flask
flask_app = Flask(__name__)

app = Api(app = flask_app, 
		  version = "1.0", 
		  title = "", 
		  description = "")

api = app.namespace('race', description='CRUD Race')

# declaraçao dos tipos de dados aceitos pelo metodo post
create = api.model('create', {
    "name":fields.String(),
    "description":fields.String(),
    "restriction": fields.List(fields.String),
    "exclusiveSkills": fields.List(fields.String)
},
)

delete = api.model('delete', {
    "_id":fields.String()
})

update = api.model('update', {
    "_id":fields.String(),
    "name":fields.String(),
    "description":fields.String(),
    "restriction": fields.List(fields.String),
    "exclusiveSkills": fields.List(fields.String)
})

@api.route('/')
class race(Resource):
    def get(self):
        return raceController.get_race_list()

    @api.doc("Race creation")
    @api.expect(create)
    def post(self):
        data = request.get_json()
        result = raceController.create_race(data)
        return result;

    @api.doc("Race delete")
    @api.expect(delete)
    def delete(self):
        data = request.get_json()
        result =  raceController.delete_race(data)
        return result

    @api.doc("Race update")
    @api.expect(update)
    def put(self):
        data = request.get_json()
        result = raceController.update_race(data)
        return result;  

    
    @api.doc("Get information of a specific race")
    @api.route('/<string:id>', methods=["GET"])
    class raceRead(Resource):
        
        def get(self,id):
            result = raceController.read_race(id)
            return result;