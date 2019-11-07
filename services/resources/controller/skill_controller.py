
from services.base_controller import BaseController
from models.skill import SkillFactory
from flask_restplus import reqparse

class SkillController(BaseController):
    def set_new_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('attack_bonus')
        self.parser.add_argument('attack_dices',  action='append')
        self.parser.add_argument('attack_range')
        self.parser.add_argument('casting_time')
        self.parser.add_argument('damage')
        self.parser.add_argument('depends_on_skills', action='append')
        self.parser.add_argument('description', required=True)
        self.parser.add_argument('duration')
        self.parser.add_argument('is_material')
        self.parser.add_argument('is_somatic')
        self.parser.add_argument('is_verbal')
        self.parser.add_argument('level')
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('regeneration')
        self.parser.add_argument('school')
        self.parser.add_argument('usage_type', required=True)

        return self.parser


    def set_edit_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('attack')
        self.parser.add_argument('depends_on_skills', required=True)
        self.parser.add_argument('description', required=True)
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('usage_type', required=True)

        return self.parser




