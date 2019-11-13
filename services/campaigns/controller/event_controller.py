
from base.controller import BaseController

from flask_restplus import reqparse


class EventController(BaseController):

   def set_edit_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=False)

        return self.parser



