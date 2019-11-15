import mongoengine
import mongoengine.fields as fields

class BaseCharacterSheet(mongoengine.Document):
    meta = {'collection': 'mop_character_sheet', 'allow_inheritance': True}
    charisma = fields.FloatField()
    constitution = fields.FloatField()
    dexterity = fields.FloatField()
    experience = fields.LongField()
    hit_points = fields.IntField()
    intelligence = fields.FloatField()
    items = fields.ListField(fields.StringField())
    level = fields.IntField()
    skills = fields.ListField(fields.StringField())
    strength = fields.FloatField()
    wisdom = fields.FloatField()


class CharacterSheet(BaseCharacterSheet):
    character_class = fields.StringField()
    description = fields.StringField()
    name = fields.StringField()
    owner = fields.StringField(required=True)
    race = fields.StringField()

    def restore(self, memento):
        """
        Restores the Originator's state from a memento object.
        """

        self.hit_points = memento.get_hit_points()
        self.update()

class ConcreteCharacterMemento(BaseCharacterSheet):

    date = fields.DateTimeField()
