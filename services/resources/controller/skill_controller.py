from json import dumps, loads
from models.skill import Skill

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
        parser.add_argument('depends_on_skills', required=True)
        parser.add_argument('attack')
        parse_result = parser.parse_args(req=self.request)

        # Document.from_json() gets a string as an argument, so we need to use `json.dumps()` here
        Skill.from_json(dumps(parse_result)).save()

        return parse_result

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
        parser.add_argument('name', required=True)
        parser.add_argument('usage_type', required=True)
        parser.add_argument('description', required=True)
        parser.add_argument('depends_on_skills', required=True)
        parser.add_argument('attack')
        parse_result = parser.parse_args(req=self.request)

        no_docs_updated = skill.update(**parse_result)

        if no_docs_updated == 1:  # the row was updated successfully
            updated_skill = Skill.objects.get(id=identifier)
            return loads(updated_skill.to_json())

    @staticmethod
    def delete(identifier):
        """
        Deletes an skill given its id
        """
        target = Skill.objects.get(id=identifier)
        target_data = loads(target.to_json())

        target.delete()

        return target_data

    @staticmethod
    def get_element_detail(identifier):
        """
        Returns an item matching the given id
        """
        return Skill.objects.get(id=identifier).to_json()

