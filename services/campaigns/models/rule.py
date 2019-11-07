import mongoengine
import mongoengine.fields as fields


class Rule(mongoengine.Document):
    meta = {'collection': 'mop_rule'}
    name = fields.StringField(required=True)
    description = fields.StringField()
    races = fields.ListField()
    character_classes = fields.ListField()
    skills = fields.ListField()
    items = fields.ListField()
 