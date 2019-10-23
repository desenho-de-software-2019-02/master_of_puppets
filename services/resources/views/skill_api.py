import json

from flask_restplus import Namespace
from flask_restplus import Resource
from flask_restplus import fields

from flask import request
from flask import jsonify

from mongoengine import DoesNotExist
from mongoengine import ValidationError

from controller.skill_controller import SkillController


api = Namespace('skills', description='Skill namespace')

skill_model = api.model('Skill', {
    'name': fields.String(required=True, description='Skill name'),
    'usage_type': fields.String(required=True, description='Usage type'),
    'description': fields.String(required=True, description='Skill description'),
    'depends_on_skills': fields.List(fields.String),
})


@api.route('/')
class SkillList(Resource):
    @api.doc("Item List")
    def get(self):
        controller = SkillController(request)
        query = controller.list()

        return jsonify(query)

    @api.doc("Skill creation")
    @api.expect(skill_model)
    def post(self):
        controller = SkillController(request)
        args = controller.new()

        return args


@api.route('/<string:id>')
@api.response(200, 'Success')
@api.response(400, 'Skill not found')
@api.param('id', 'Skill identifier')
class SkillDetail(Resource):
    param = "An integer that represents the skill's id"

    @api.doc("Get information of a specific skill", params={'id': param})
    @api.response(400, 'Skill not found')
    def get(self, id):
        controller = SkillController(request)

        try:
            skill = controller.get_element_detail(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Skill with id {} does not exist".format(id))

        return json.loads(skill)

    @api.doc("Update an skill", params={'id': param})
    @api.expect(skill_model)
    def put(self, id):
        controller = SkillController(request)

        try:
            new_skill = controller.edit(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Skill with id {} does not exist".format(id))

        return new_skill

    @api.doc("Delete an skill", params={'id': param})
    def delete(self, id):
        controller = SkillController(request)
        deleted = controller.delete(id)

        return deleted
