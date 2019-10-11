from flask_restplus import Namespace, Resource, Api, fields
from core import race_controller
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
class raceList(Resource):
    def get(self):
        return race_controller.get_race_list()

@api.route("/create")

class raceCreate(Resource):
    @api.expect(create)
    def post(self):
        data = request.get_json()
        result = race_controller.create_race(data)
        return result;



@api.route('/delete',methods=["DELETE"])
class raceDelete(Resource):
    @api.expect(delete)
    def delete(self):
        data = request.get_json()
        result =  race_controller.delete_race(data)
        return result

@api.route('/update',methods=["PUT"])
class raceUpdate(Resource):
    @api.expect(update)
    def put(self):
        data = request.get_json()
        result = race_controller.update_race(data)
        return result;  

@api.route('/read/<string:id>', methods=["GET"])
class raceRead(Resource):
    
    def get(self,id):
        result = race_controller.read_race(id)
        return result;