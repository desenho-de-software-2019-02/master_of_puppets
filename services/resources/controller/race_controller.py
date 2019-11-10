
from base.controller import Strategy

from flask_restplus import reqparse


class RaceController(Strategy):


    def set_edit_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('description', required=False)
        self.parser.add_argument('exclusive_skills', type=list, required=False)
        self.parser.add_argument('name', required=False)
        self.parser.add_argument('restrictions', type=list, required=False)

        return self.parser



