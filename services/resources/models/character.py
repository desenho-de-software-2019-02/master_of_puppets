import mongoengine
import mongoengine.fields as fields


class Character(mongoengine.Document):
    meta = {'collection': 'mop_character'}
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
