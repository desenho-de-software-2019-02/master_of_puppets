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


api = Namespace('race', description='Race routes')

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
    @api.doc("Race list")
    def get(self):
        controller = RaceController(request)
        query = controller.list()

        return jsonify(query)

    @api.doc("Race creation")
    @api.expect(create)
    def post(self):
        controller = RaceController(request)
        args = controller.new()

        return args


@api.route('/<string:id>')
@api.response(200, 'Success')
@api.response(400, 'Race not found')
@api.param('id', 'Race identifier')
class RaceDetail(Resource):
    param = "A string that represents the race's id"

    @api.doc("Race delete", params={'id': param})
   
    def delete(self,id):
        controller = RaceController(request)
        deleted = controller.delete(id)

        return deleted 

    @api.doc("Race update", params={'id': param})
    @api.expect(update)
    @api.response(200, 'Success')
    @api.response(400, 'Race not found')
    def put(self, id):
        controller = RaceController(request)

        try:
            new_item = controller.edit(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Item with id {} does not exist".format(id))

        return new_item

    @api.doc("Get information of a specific item", params={'id': param})
    @api.response(200, 'Success')
    @api.response(400, 'Race not found')
    def get(self, id):
        controller = RaceController(request)

        try:
            race = controller.get_element_detail(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Race with id {} does not exist".format(id))

        return json.loads(race)
