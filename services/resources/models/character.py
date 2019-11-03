import mongoengine
import mongoengine.fields as fields

mongoengine.connect('dev', host='mongodb://root:root@0.0.0.0:27017/mop')


class Character(mongoengine.Document):
    # Maybe will be necessary to switch ReferenceFields for LazyReferenceFields
    name = fields.StringField()
    description = fields.StringField()
    hit_points = fields.IntField()
    level = fields.IntField()
    experience = fields.LongField()
    attributes = fields.ReferenceField('Attributes')
    race = fields.ReferenceField('Race')
    character_class = fields.ReferenceField('CharacterClass')
    skills = fields.ListField(fields.ReferenceField('Skill'))
    items = fields.ListField(fields.ReferenceField('Item'))
    owner = fields.ReferenceField('User')
