import json
from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify
from mongoengine import DoesNotExist, ValidationError

from controller.character_controller import CharacterController

api = Namespace('characters', description='Character namespace')

campaign_model = api.model('Campaign', {
    'name' = fields.StringField(required=True)
    'gameMaster' = fields.ObjectIdField(required=true)
    'players' = fields.ListField(fields.ObjectIdField())
    'characters' = fields.ListField(fields.ObjectIdField())
    'rules' = fields.ListField(fields.ObjectIdField())
    'session' = fields.ObjectIdField(required=true)
})

@api.route('/')
class CampaignList(Resource):
    @api.doc("Campaign List")
    def get(self):
        controller = CampaignController(request)
        query = controller.list()

        return jsonify(query)

    @api.doc("Campaign Creation")
    @api.expect(campaign_model)
    def post(self):
        controller = CampaignController(request)
        args = controller.new()

        return args

@api.route('/<string:id>')
@api.response(200, 'Success')
@api.response(400, 'Item not found')
@api.param('id', 'Item identifier')

class ItemDetail(Resource):
    param = "An integer that represents the campaign's id"

    @api.doc("Get information on a specific campaign")
    @api.response(400, 'Campaign not found')
    def get(self, identifier):
        controller = CampaignController

        try:
            campaign = controller.get_element_detail(identifier)
        except (DoesNotExist, ValidationError):
            api.abort(400, 'Campaign with id {} does not exist')

        return json.loads(campaign)
    
    @api.doc("Update an campaign", params={'id': param})
    @api.expect(campaign_model)
    def put(self, identifier)
        controller = CampaignController

        try:
            new_campaign = controller.edit(identifier)
        except(DoesNotExist, ValidationError):
            api.abort(400, "Campaign with id {} does not exist")
        
        return new_campaign

    @api.doc("Delete a campaign", params{'id': param})
    def delete(self, identifier):
        controller = CampaignController
        deleted = controller.delete(identifier)

        return deleted