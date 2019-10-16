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

    @staticmethod
    def list():
        """
        Makes a query to list all skills
        """

        list_of_skills = list(map(lambda skill: loads(skill.to_json()), skill.objects.all()))
        return list_of_skills

    def edit(self, identifier):
        """
        Edits an skill given its id
        """
        
        skill = skill.objects.get(id=identifier)

        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('usage_type', required=True)
        parser.add_argument('description', required=True)
        parser.add_argument('depends_on_items', required=True)
        parse_result = parser.parse_args(req=self.request)

        no_docs_updated = skill.update(**parse_result)

        if no_docs_updated == 1:  # the row was updated successfully
            return loads(skill.to_json())

    @staticmethod
    def delete(identifier):
        """
        Deletes an skill given its id
        """
        target = skill.objects.get(id=identifier)
        target_data = loads(target.to_json())

        target.delete()

        return target_data
