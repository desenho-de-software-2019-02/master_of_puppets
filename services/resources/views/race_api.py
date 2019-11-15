import json

from flask_restplus import Api
from flask_restplus import fields
from flask_restplus import Resource
from flask_restplus import Namespace

from flask import Flask
from flask import request
from flask import jsonify

from mongoengine import DoesNotExist
from mongoengine import ValidationError
from controller.race_controller import RaceController
from models.race import Race

api = Namespace('races', description='Race routes namespace')

def get_controller():
	controller = RaceController(model=Race, request=request)
	return controller

create = api.model('create', {
    "name": fields.String(),
    "description": fields.String(),
    "restriction": fields.List(fields.String),
    "exclusiveSkills": fields.List(fields.String)
},
)

update = api.model('update', {
    "name": fields.String(),
    "description": fields.String(),
    "restriction": fields.List(fields.String),
    "exclusiveSkills": fields.List(fields.String)
})


@api.route('/')
class RaceList(Resource):

    @api.doc("Race list_elements")
    def get(self):
        controller = get_controller()
        query = controller.list_elements()

        return jsonify(query)

    @api.doc("Race creation")
    @api.expect(create)
    def post(self):
        controller = get_controller()
        args = controller.new()

        return {'id': args}


@api.route('/<string:id>')
@api.response(200, 'Success')
@api.response(400, 'Race not found')
@api.param('id', 'Race identifier')
class RaceDetail(Resource):

    param = "A string that represents the race's id"

    @api.doc("Race delete", params={'id': param})
    def delete(self, id):
        controller = get_controller()
        deleted = controller.delete(id)

        return deleted

    @api.doc("Race update", params={'id': param})
    @api.expect(update)
    @api.response(200, 'Success')
    @api.response(400, 'Race not found')
    def put(self, id):
        controller = get_controller()

        try:
            new_item = controller.edit(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Item with id {} does not exist".format(id))

        return new_item

    @api.doc("Get information of a specific item", params={'id': param})
    @api.response(200, 'Success')
    @api.response(400, 'Race not found')
    def get(self, id):
        controller = get_controller()

        try:
            race = controller.get_element_detail(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Race with id {} does not exist".format(id))

        return json.loads(race)