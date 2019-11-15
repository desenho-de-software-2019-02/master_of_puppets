from json import dumps, loads
import mongoengine.fields
from flask_restplus import reqparse

class BaseController():

    def __init__(self, request, model):
        self.request = request
        self.model = model

    def set_default_parser(self):
        self.default_parser = reqparse.RequestParser()

        for field_name, field_type in self.model._fields.items():
            if field_name == '_cls':
                continue
            if isinstance(field_type, mongoengine.fields.ListField):
                self.default_parser.add_argument(field_name, required=field_type.required, action='append')
            else:
                self.default_parser.add_argument(field_name, required=field_type.required)

    @staticmethod
    def get_default_parser(self):
        return self.default_parser

    def get_unique(self, identifier):
        return self.model.objects.get(id=identifier)

    def new(self):
        self.set_default_parser()
        parser = self.get_default_parser(self)
        parse_result = parser.parse_args(req=self.request)

        self.model.from_json(dumps(parse_result)).save()

        return parse_result

    def list_elements(self):
        list_of_elements = list(map(lambda element: loads(element.to_json()), self.model.objects.all()))
        return list_of_elements

    def get_element_detail(self, identifier):
        return self.get_unique(identifier).to_json()

    def edit(self, identifier):
        element = self.get_unique(identifier)
        parser = self.set_edit_parser()
        parse_result = parser.parse_args(req=self.request)
        no_docs_updated = element.update(**parse_result)
        if no_docs_updated == 1:  # the row was updated successfully
            return loads(element.to_json())

    def delete(self, identifier):
        target = self.get_unique(identifier)
        target_data = loads(target.to_json())
        target.delete()
        return target_data

    def set_edit_parser(self):
        pass
