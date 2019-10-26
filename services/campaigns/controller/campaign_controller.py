from flask_restplus import reqparse
from services.strategy import Strategy

class CampaignController(Strategy):
    def set_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('gameMaster', required=True)
        self.parser.add_argument('players', action='append')
        self.parser.add_argument('characters', action='append')
        self.parser.add_argument('rules', action='append')
        self.parser.add_argument('session')
        return self.parser