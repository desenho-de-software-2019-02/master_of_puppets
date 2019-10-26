from flask_restplus import reqparse
from services.strategy import Strategy

class RuleController(Strategy):
    def set_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('description')
        self.parser.add_argument('races', action='append')
        self.parser.add_argument('klasses', action='append')
        self.parser.add_argument('skills', action='append')
        self.parser.add_argument('items', action='append') 
        return self.parser
