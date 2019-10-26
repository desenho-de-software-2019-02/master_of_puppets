from flask_restplus import reqparse
from services.strategy import Strategy

class CharacterController(Strategy):
    def set_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('description')
        self.parser.add_argument('hit_points')
        self.parser.add_argument('level')
        self.parser.add_argument('experience')
        self.parser.add_argument('strength')
        self.parser.add_argument('desterity')
        self.parser.add_argument('costitution')
        self.parser.add_argument('intelligence')
        self.parser.add_argument('wisdom')
        self.parser.add_argument('charisma')
        self.parser.add_argument('race')
        self.parser.add_argument('klass')
        self.parser.add_argument('skills', action='append')
        self.parser.add_argument('items', action='append') 
        self.parser.add_argument('owner')
        return self.parser
