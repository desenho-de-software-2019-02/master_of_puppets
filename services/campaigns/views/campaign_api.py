from flask_restplus import Namespace, Resource, Api, fields
from core.campaign_controller import campaignController
from flask import request, jsonify,Flask
flask_app = Flask(__name__)

app = Api(app = flask_app, 
		  version = "1.0", 
		  title = "", 
		  description = "")

api = app.namespace('campaign', description='CRUD Match')

# declaraçao dos tipos de dados aceitos pelo metodo post
create = api.model('create', {
    "gameMaster": fields.String(),
    "players": fields.List(fields.String),
    "characters": fields.List(fields.String),
    "rules": fields.List(fields.String),
    "session": fields.String(),
    "date_initial": fields.DateTime(dt_format='rfc862')},
)

delete = api.model('delete', {
    "_id":fields.String()
})

update = api.model('update', {
    "_id":fields.String(),
    "gameMaster": fields.String(),
    "players": fields.List(fields.String),
    "characters": fields.List(fields.String),
    "rules": fields.List(fields.String),
    "session": fields.String(),
})

@api.route('/')
class campaignList(Resource):
    def get(self):
        return campaignController.get_campaigns()
    @api.expect(create)
    def post(self):
        data = request.get_json()
        response = campaignController.create_campaign(data)
        return response

#WORK IN PROGRESS
# @api.route('/delete',methods=["DELETE"])
# class campaignDelete(Resource):
#     @api.expect(delete)
#     def delete(self):
#         data = request.get_json()
#         response =  campaignController.delete_campaign(data)
#         return response