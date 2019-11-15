import mongoengine
import mongoengine.fields as fields


class CharacterClass(mongoengine.Document):

    meta = {'collection': 'mop_class'}


    name = fields.StringField()
    description = fields.StringField()
    restrictions = fields.ListField(
    fields.ReferenceField('Skill'), required=False)
    effects = fields.ListField(fields.ReferenceField('Skill'), required=False)
    exclusive_skills = fields.ListField(
    fields.ReferenceField('Skill'), required=False)
