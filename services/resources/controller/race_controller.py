from flask_restplus import reqparse
from services.strategy import Strategy

class RaceController(Strategy):
    def set_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('description', required=True)
        self.parser.add_argument('restrictions', type=list)
        self.parser.add_argument('exclusive_skills', type=list)
        return self.parser
