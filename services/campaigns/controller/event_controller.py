
from base.controller import BaseController

from flask_restplus import reqparse

class EventController(BaseController):

   def set_edit_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('event_type', required=True)
        self.parser.add_argument('description', required=True)
        self.parser.add_argument('event_date', required=True)
        self.parser.add_argument('data', required=False)

        return self.parser
