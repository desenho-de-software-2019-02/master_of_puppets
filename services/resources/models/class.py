import mongoengine
import mongoengine.fields as fields



class Klass(mongoengine.Document):
    meta = {'collection': 'mop_class'}
    name = fields.StringField()
    description = fields.StringField()
    restrictions = fields.ListField(fields.ReferenceField('Skill'))
    exclusive_skills = fields.ListField(fields.ReferenceField('Skill'))
