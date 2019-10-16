import mongoengine
import mongoengine.fields as fields

mongoengine.connect('dev', host='mongodb://root:root@0.0.0.0:27017/mop')


class Rule(mongoengine.Document):
    name = fields.StringField(required=True)
    description = fields.StringField()
    races = fields.ListField(fields.ReferenceField('Race'),
                             required=True)
    klasses = fields.ListField(
        fields.ReferenceField('Klass'), required=True)
    skills = fields.ListField(fields.ReferenceField('Skill'), required=True)
    items = fields.ListField(fields.ReferenceField('Item'), required=True)
