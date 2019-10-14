import mongoengine
import mongoengine.fields as fields

mongoengine.connect('dev', host='mongodb://root:root@0.0.0.0:27017/mop')


class Attribute(mongoengine.Document):
    meta = {'collection': 'mop_attributes'}
    strength = fields.IntField(min_value=0)
    dexterity = fields.IntField(min_value=0)
    constitution = fields.IntField(min_value=0)
    intelligence = fields.IntField(min_value=0)
    wisdom = fields.IntField(min_value=0)
    charisma = fields.IntField(min_value=0)
