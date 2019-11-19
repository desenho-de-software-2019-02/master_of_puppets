
from flask_restplus import reqparse
from base.controller import BaseController

class CharacterClassController(BaseController):

    def set_edit_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=False)
        self.parser.add_argument('description', required=False)
        self.parser.add_argument('restrictions', action='append', required=False)
        self.parser.add_argument('effects', action='append', required=False)
        self.parser.add_argument('exclusive_skills', action='append', required=False)

        return self.parser

