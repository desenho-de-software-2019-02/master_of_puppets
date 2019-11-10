from services.base_controller import Strategy

from flask_restplus import reqparse

class CampaignController(Strategy):
    def set_new_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('characters', action='append')
        self.parser.add_argument('gameMaster', required=True)
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('players', action='append')
        self.parser.add_argument('rules', action='append')
        self.parser.add_argument('session')

        return self.parser


    def set_edit_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('characters', required=False)
        self.parser.add_argument('gameMaster', required=False)
        self.parser.add_argument('name', required=False)
        self.parser.add_argument('players', required=False)
        self.parser.add_argument('rules', required=False)
        self.parser.add_argument('session', required=False)

        return self.parser
