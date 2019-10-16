from json import dumps, loads
from models.skill import skill

from flask_restplus import reqparse


class SkillController:
    def __init__(self, request):
        self.request = request

    def new(self):
        """
        Creates a new skill
        """
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('usage_type', required=True)
        parser.add_argument('description', required=True)
        parser.add_argument('depends_on_items', required=True)
        parse_result = parser.parse_args(req=self.request)

        # Document.from_json() gets a string as an argument, so we need to use `json.dumps()` here
        skill.from_json(dumps(parse_result)).save()

        return parse_result

