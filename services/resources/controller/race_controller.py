
from services.base_controller import Strategy

from flask_restplus import reqparse


class RaceController(Strategy):
    def set_new_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('description', required=True)
        self.parser.add_argument('exclusive_skills', type=list)
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('restrictions', type=list)

        return self.parser


    def set_edit_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('description', required=False)
        self.parser.add_argument('exclusive_skills', type=list, required=False)
        self.parser.add_argument('name', required=False)
        self.parser.add_argument('restrictions', type=list, required=False)

        return self.parser



