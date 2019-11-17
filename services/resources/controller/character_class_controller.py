
from flask_restplus import reqparse
from base.controller import BaseController

class CharacterClassController(BaseController):

    def set_edit_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('description', required=True)
        self.parser.add_argument('effects', action='append', required=True)
        self.parser.add_argument('exclusive_skills', action='append', required=True)
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('restrictions', action='append', required=True)

        return self.parser
