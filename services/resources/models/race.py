import mongoengine
import mongoengine.fields as fields

from models.base_document import BaseDocument


class Race(BaseDocument):
    meta = {'collection': 'mop_races'}

    name = fields.StringField(required=True)
    description = fields.StringField(required=True)
    restrictions = fields.ListField(fields.ReferenceField('Skill'), required=False)
    exclusive_skills = fields.ListField(fields.ReferenceField('Skill'), required=False)
