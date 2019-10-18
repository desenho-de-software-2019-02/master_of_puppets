import mongoengine
import mongoengine.fields as fields


class Rule(mongoengine.Document):
    meta = {'collection': 'mop_rule'}
    name = fields.StringField(required=True)
    description = fields.StringField()
    races = fields.ListField(fields.StringField,
                             required=False)
    klasses = fields.ListField(fields.StringField, required=False)
    skills = fields.ListField(fields.StringField, required=False)
    items = fields.ListField(fields.StringField, required=False)
