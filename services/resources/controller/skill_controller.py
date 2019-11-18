from base.controller import BaseController
from json import dumps
from models.skill import SkillFactory
from flask_restplus import reqparse
import logging

class SkillController(BaseController):

    def new(self):
        """
        Creates a new skill
        """
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('description', required=True)
        parser.add_argument('depends_on_skills', action='append')
        parser.add_argument('regeneration_multiplier')
        parser.add_argument('attack_multiplier')
        parser.add_argument('defense_multiplier')
        parser.add_argument('attack_bonus')
        parser.add_argument('attack_range')
        parser.add_argument('attack_dices',  action='append')
        parser.add_argument('level')
        parser.add_argument('school')
        parser.add_argument('is_verbal')
        parser.add_argument('is_somatic')
        parser.add_argument('is_material')

        parse_result = parser.parse_args(req=self.request)

        factory = SkillFactory(parse_result)
        item_class = factory.create_skill()
        item_data = factory.get_data()
        # item_class.from_json(dumps(item_data)).save()
        # Document.from_json() gets a string as an argument, so we need to use `json.dumps()` here
        item = item_class.from_json(dumps(parse_result)).save()
        item_data['type'] = str(item_class)

        return "{}".format(item.id)

    @staticmethod
    def list():
        """
        Makes a query to list all skills
        """

        list_of_skills = list(map(lambda skill: loads(skill.to_json()), Skill.objects.all()))
        return list_of_skills

    def edit(self, identifier):
        """
        Edits an skill given its id
        """
        skill = Skill.objects.get(id=identifier)

        parser = reqparse.RequestParser()
        parser.add_argument('name',required=False)
        parser.add_argument('description',required=False)
        parser.add_argument('depends_on_skills', action='append',required=False)
        parser.add_argument('regeneration_multiplier',required=False)
        parser.add_argument('attack_multiplier',required=False)
        parser.add_argument('defense_multiplier',required=False)
        parser.add_argument('attack_bonus', type=int, required=False)
        parser.add_argument('attack_range',required=False)
        parser.add_argument('attack_dices',  action='append',required=False)
        parser.add_argument('level',required=False)
        parser.add_argument('school',required=False)
        parser.add_argument('is_verbal',required=False)
        parser.add_argument('is_somatic',required=False)
        parser.add_argument('is_material',required=False)
        parse_result = parser.parse_args(req=self.request)

        factory = SkillFactory(parse_result)
        factory.create_skill()
        edited_skill = factory.get_data()

        try:
            no_docs_updated = skill.update(**edited_skill)
        except Exception as e:
            logging.error(e)

        if no_docs_updated == 1:  # the row was updated successfully
            updated_skill = Skill.objects.get(id=identifier)
            return loads(updated_skill.to_json())

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
