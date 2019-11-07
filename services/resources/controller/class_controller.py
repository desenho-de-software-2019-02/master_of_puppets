
from models.character_class import CharacterClass

from flask_restplus import reqparse


class ClassController(BaseController):
    def set_new_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('description', required=True)
        self.parser.add_argument('effects', action='append')
        self.parser.add_argument('exclusive_skills', action='append')
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('restrictions', action='append')

        return self.parser


    def set_edit_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('description', required=True)
        self.parser.add_argument('effects', type=list, required=True)
        self.parser.add_argument('exclusive_skills', type=list, required=True)
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('restrictions', type=list, required=True)

        return self.parser



