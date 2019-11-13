import json
from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify
from mongoengine import DoesNotExist, ValidationError

from controller.match_controller import MatchController

from models.match import Match

api = Namespace('matches', description='Match namespace')


def get_controller():
	controller = MatchController(model=Match, request=request)
	return controller


match_model = api.model('Match', {
    'name': fields.String(required=True, description='Match name'),
    'events': fields.List(fields.String(), description='Match events'),
    'description': fields.String(description='Match description')
})

@api.route('/')
class MatchList(Resource):
    @api.doc("Match List")
    def get(self):
        controller = get_controller()
        query = controller.list_elements()

        return jsonify(query)

    @api.doc("Match creation")
    @api.expect(match_model)
    def post(self):
        controller = get_controller()
        args = controller.new()

        return args


@api.route('/<string:id>')
@api.response(200, 'Success')
@api.response(400, 'Match not found')
@api.param('id', 'Match identifier')
class MatchDetail(Resource):
    param = "An integer that represents the match's id"

    @api.doc("Get information of a specific match", params={'id': param})
    @api.response(400, 'Match not found')
    def get(self, id):
        controller = get_controller()

        try:
            match = controller.get_element_detail(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Match with id {} does not exist".format(id))

        return json.loads(match)

    @api.doc("Update an match", params={'id': param})
    @api.expect(match_model)
    def put(self, id):
        controller = get_controller()

        try:
            new_match = controller.edit(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Match with id {} does not exist".format(id))

        return new_match

    @api.doc("Delete an match", params={'id': param})
    def delete(self, id):
        controller = get_controller()
        deleted = controller.delete(id)

        return deleted
