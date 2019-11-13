from base.controller import BaseController

from flask_restplus import reqparse

class CampaignController(BaseController):


    def set_edit_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=False)
        self.parser.add_argument('gameMaster', required=False)
        self.parser.add_argument('players', required=False)
        self.parser.add_argument('characters', required=False)
        self.parser.add_argument('rules', required=False)

        return self.parser
