import json
from flask_restplus import Namespace, Resource, fields
from flask import request, jsonify
from mongoengine import DoesNotExist, ValidationError

from controller.skill_controller import SkillController

from models.skill import Skill

api = Namespace('skills', description='Skill namespace')

def get_controller():
	controller = SkillController(model=Skill, request=request)
	return controller

skill_model = api.model('Skill', {
    'attack_dices' : fields.List(fields.String()),
    'attack_multiplier': fields.String(description='Attribute used as attack multiplier'),
    'bonus_attack' : fields.Integer(description='Integer that boosts attack calculation'),
    'defense_multiplier': fields.String(description='Attribute used as defense multiplier'),
    'depends_on_skills' :  fields.List(fields.String),
    'description' : fields.String(required=True, description='Skill description'),
    'is_material' : fields.Boolean(),
    'is_somatic' : fields.Boolean(),
    'is_verbal' : fields.Boolean(),
    'level' : fields.Integer(),
    'name' : fields.String(required=True, description='Skill name'),
    'regeneration_multiplier': fields.String(description='Attribute used as regen multiplier'),
    'school' : fields.String()
})


@api.route('/')
class SkillList(Resource):
    @api.doc("List of Skills")
    def get(self):
        controller = get_controller()
        query = controller.list_elements()

        return jsonify(query)

    @api.doc("Skill creation")
    @api.expect(skill_model)
    def post(self):
        controller = get_controller()
        args = controller.new()

        return {"id": args}


@api.route('/<string:id>')
@api.response(200, 'Success')
@api.response(400, 'Skill not found')
@api.param('id', 'Skill identifier')
class SkillDetail(Resource):

    param = "An integer that represents the skill's id"

    @api.doc("Get information of a specific skill", params={'id': param})
    @api.response(400, 'Skill not found')
    def get(self, id):
        controller = get_controller()

        try:
            skill = controller.get_element_detail(id)
        except (DoesNotExist, ValidationError):
            api.abort(400, "Skill with id {} does not exist".format(id))

        return json.loads(skill)

    @api.doc("Update an skill", params={'id': param})
    @api.expect(skill_model)
    def put(self, id):
        controller = get_controller()

        new_skill = controller.edit(id)

        return new_skill

    @api.doc("Delete an skill", params={'id': param})
    def delete(self, id):
        controller = get_controller()
        deleted = controller.delete(id)

        return deleted
