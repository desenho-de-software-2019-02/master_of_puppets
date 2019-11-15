import abc
import mongoengine
import mongoengine.fields as fields

from models.character import Character


class CombatManager(mongoengine.Document):
    mongoengine.connect(
        db='mop', host='mongodb://mongo_main:27017/mop', alias='campaigns')
    meta = {'collection': 'mop_combat', 'db_alias': 'campaigns'}

    turn_list = fields.ListField(fields.ReferenceField('Turn'))
    active_turn = fields.ReferenceField('Turn')


class Turn(mongoengine.Document):
    mongoengine.connect(
        db='mop', host='mongodb://mongo_main:27017/mop', alias='campaigns')

    meta = {'allow_inheritance': True,
            'collection': 'mop_combat', 'db_alias': 'campaigns'}

    class Meta:
        abstract = True


class CharacterTurn(Turn):
    character = fields.LazyReferenceField('Character')
