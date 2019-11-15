import mongoengine
import mongoengine.fields as fields


class Race(mongoengine.Document):
    meta = {'collection': 'mop_races'}
    
    name = fields.StringField(required=True)
    description = fields.StringField(required=True)
    restrictions = fields.ListField(fields.ReferenceField('Skill'), required=False)
    exclusive_skills = fields.ListField(fields.ReferenceField('Skill'), required=False)
