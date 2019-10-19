import mongoengine
import mongoengine.fields as fields

class Klass(mongoengine.Document):
    meta = {'collection': 'mop_class'}
    name = fields.StringField()
    description = fields.StringField()
    restrictions = fields.ListField(fields.StringField())
    effects = fields.ListField(fields.StringField())
    exclusive_skills = fields.ListField(fields.StringField())
