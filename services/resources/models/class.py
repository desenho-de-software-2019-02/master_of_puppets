import mongoengine
import mongoengine.fields as fields

mongoengine.connect('dev', host='mongodb://root:root@0.0.0.0:27017/mop')


class Klass(mongoengine.Document):
    meta = {'collection': 'mop_class'}
   
    name = fields.StringField()
    description = fields.StringField()
    restrictions = fields.ListField(fields.ReferenceField('Skill'))
    exclusive_skills = fields.ListField(fields.ReferenceField('Skill'))
