
from base.controller import Strategy
from models.skill import SkillFactory
from flask_restplus import reqparse

class SkillController(Strategy):


    def set_edit_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('attack')
        self.parser.add_argument('depends_on_skills', required=True)
        self.parser.add_argument('description', required=True)
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('usage_type', required=True)

        return self.parser




