
from services.base_controller import BaseController

from flask_restplus import reqparse


class MatchController(BaseController):
    def set_new_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('description')
        self.parser.add_argument('events', action='append')
        self.parser.add_argument('name', required=True)

        return self.parser


    def set_edit_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('description')
        self.parser.add_argument('events', action='append')
        self.parser.add_argument('name', required=True)

        return self.parser



