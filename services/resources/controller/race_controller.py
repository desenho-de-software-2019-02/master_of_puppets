from base.controller import BaseController
from flask_restplus import reqparse

class RaceController(BaseController):

    def set_edit_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('description', required=False)
        self.parser.add_argument('exclusive_skills', required=False, action='append')
        self.parser.add_argument('name', required=False)
        self.parser.add_argument('restrictions', required=False, action='append')

        return self.parser
