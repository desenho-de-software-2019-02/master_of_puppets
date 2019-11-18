import mongoengine.fields as fields

from models.base_document import BaseDocument


class CharacterClass(BaseDocument):
    meta = {'collection': 'mop_class'}

    name = fields.StringField()
    description = fields.StringField()
    restrictions = fields.ListField(
    fields.ReferenceField('Skill'), required=False)
    effects = fields.ListField(fields.ReferenceField('Skill'), required=False)
    exclusive_skills = fields.ListField(
    fields.ReferenceField('Skill'), required=False)
