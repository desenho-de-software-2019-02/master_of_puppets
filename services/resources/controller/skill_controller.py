from base.controller import BaseController
from json import dumps
from models.skill import SkillFactory
from flask_restplus import reqparse

class SkillController(BaseController):


    def new(self):
        self.set_default_parser()
        parser = self.get_default_parser(self)
        parse_result = parser.parse_args(req=self.request)

        factory = SkillFactory(parse_result)
        item_class = factory.create_skill()

        item_data = factory.get_data()

        self.model.from_json(dumps(parse_result)).save()
        item_data['type_of_skill'] = str(item_class)


        return parse_result


    def set_edit_parser(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('attack')
        self.parser.add_argument('depends_on_skills', required=True)
        self.parser.add_argument('description', required=True)
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('usage_type', required=True)

        return self.parser
