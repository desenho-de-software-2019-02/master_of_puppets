from json import dumps, loads
from models.rule import Rule

from flask_restplus import reqparse

class RuleController:
    def __init__(self, request):
        self.request = request
    
    def new(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('description')
        parser.add_argument('races', action='append')
        parser.add_argument('klasses', action='append')
        parser.add_argument('skills', action='append')
        parser.add_argument('items', action='append') 
        parse_result = parser.parse_args(req=self.request)

        print("*"*100 )
        print(type(parse_result))
 
        Rule.from_json(dumps(parse_result)).save()

        return parse_result

    @staticmethod
    def list():
        """
        Makes a query to list all rules
        """

        list_of_rules = list(map(lambda rule: loads(rule.to_json() ), Rule.objects.all()))
        return list_of_rules

    @staticmethod
    def get_element_detail(identifier):
        """
        Returns an rule matching the given id
        """
        return Rule.objects.get(id=identifier).to_json()
    
    def edit(self, identifier):
        """
        Edits an rule given its id
        """
        rule = Rule.objects.get(id=identifier)

        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('description')
        parser.add_argument('races', action='append')
        parser.add_argument('klasses', action='append')
        parser.add_argument('skills', action='append')
        parser.add_argument('items', action='append') 
        parse_result = parser.parse_args(req=self.request)

        no_docs_updated = rule.update(**parse_result)

        if no_docs_updated == 1:  # the row was updated successfully
            rule = Rule.objects.get(id=identifier)
            return loads(rule.to_json())

    @staticmethod
    def delete(identifier):
        """
        Deletes an rule given its id
        """
        target = Rule.objects.get(id=identifier)
        target_data = loads(target.to_json())

        target.delete()

        return target_data
