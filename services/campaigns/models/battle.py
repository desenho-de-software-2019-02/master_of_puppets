import abc
import mongoengine
import mongoengine.fields as fields


class CombatManager(mongoengine.Document):
    turn_list = fields.ListField(fields.ReferenceField('Turn'))
    active_turn = fields.ReferenceField('Turn')

    def __init__(self, turns):
        self.turn_list = turns
        self.active_turn = self.turn_list[0]

class Turn(mongoengine.Document):
    meta = {'allow_inheritance': True}
    class Meta:
        abstract = True


class CharacterTurn(Turn):
    character = fields.ReferenceField('Character')

    def __init__(self, character_id):
        self.character = character_id
