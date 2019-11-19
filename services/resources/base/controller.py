from json import dumps, loads
import mongoengine.fields
from flask_restplus import reqparse
from importlib import import_module

class BaseController():

    def __init__(self, request, model):
        self.request = request
        self.model = model
        self.get_reference_fields()

    def set_default_parser(self):
        self.default_parser = reqparse.RequestParser()

        for field_name, field_type in self.model._fields.items():
            if field_name == '_cls' or field_name == 'init_date':
                continue
            if isinstance(field_type, mongoengine.fields.ListField):
                self.default_parser.add_argument(field_name, required=field_type.required, action='append')
            else:
                self.default_parser.add_argument(field_name, required=field_type.required)

    
    def get_reference_fields(self):
        self.classes = {}
        self.list_reference_fields = {}
        self.reference_fields = {}

        for field_name, field_type in self.model._fields.items():
            if isinstance(field_type, mongoengine.fields.ReferenceField):
                print('------------------\n\n\n\n\n\n')
                print(field_type.document_type_obj)
                print('------------------\n\n\n\n\n\n')
                dto = field_type.document_type_obj
                if (isinstance(dto, str)):
                    module = {
                        '__module__': 'models.'+dto.lower(),
                        '_class_name': dto
                    }
                if (isinstance(dto, mongoengine.base.metaclasses.TopLevelDocumentMetaclass)):
                    module = dto.__dict__
                    
                classe = getattr(import_module(module['__module__']), module['_class_name'])
                
                self.classes[module['_class_name']] = classe
                self.reference_fields[field_type.name] = module['_class_name']

            if isinstance(field_type, mongoengine.fields.ListField):
                if isinstance(field_type.field, mongoengine.fields.ReferenceField):                    
                    print(field_type.field.__dict__)
                    dto = field_type.field.document_type_obj
                    if (isinstance(dto, str)):
                        module = {
                            '__module__': 'models.'+dto.lower(),
                            '_class_name': dto
                        }
                    if (isinstance(dto, mongoengine.base.metaclasses.TopLevelDocumentMetaclass)):
                        module = dto.__dict__
                        
                    classe = getattr(import_module(module['__module__']), module['_class_name'])
                    
                    self.classes[module['_class_name']] = classe
                    self.list_reference_fields[field_type.name] = module['_class_name']

        
    @staticmethod
    def get_default_parser(self):
        return self.default_parser

    def get_unique(self, identifier):
        return self.model.objects.get(id=identifier)

    def new(self):
        self.set_default_parser()
        parser = self.get_default_parser(self)
        parse_result = parser.parse_args(req=self.request)

        new_element = self.model.from_json(dumps(parse_result)).save()

        return "{}".format(new_element.id)

    def list_elements(self):
        list_of_elements = list(map(lambda element: loads(element.to_json()), self.model.objects.all()))
        return list_of_elements

    def get_element_detail(self, identifier):
        return self.get_unique(identifier).to_json()

    def edit(self, identifier):
        element = self.get_unique(identifier)
        parser = self.set_edit_parser()
        parse_result = parser.parse_args(req=self.request)
        
        parse_result = self.set_dbref(parse_result)

        no_docs_updated = element.update(**parse_result)
        if no_docs_updated == 1:  # the row was updated successfully
            new_element = self.get_unique(identifier)
            return loads(new_element.to_json())

    def set_dbref(self, parse_result):
        print(parse_result)
        for field_name, value in parse_result.items():
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n\n')
            print('nome:')
            print('\t', field_name)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
            print('valor:')
            print('\t', value)
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
            
            
            if (field_name in self.list_reference_fields.keys()):
                model = self.classes[self.list_reference_fields[field_name]]
                
                elements = []
                for field_id in value:
                    element = model.objects.get(id=field_id)
                    elements.append(element.to_dbref())
                
                parse_result[field_name] = elements
            
            if (field_name in self.reference_fields.keys()):
                model = self.classes[self.reference_fields[field_name]]
                element = model.objects.get(id=value)
                parse_result[field_name] = element.to_dbref()

        return parse_result  
                
    def delete(self, identifier):
        target = self.get_unique(identifier)
        target_data = loads(target.to_json())
        target.delete()
        return target_data

    def set_edit_parser(self):
        pass
