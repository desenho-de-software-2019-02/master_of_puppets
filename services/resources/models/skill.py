import mongoengine
import mongoengine.fields as fields

class SkillFactory:
    def __init__(self, json):
        self.json_data = json
    
    def _clean_fields(self, fields):
        for field in fields:
            self.json_data.pop(field, None)

    def get_data(self):
        return self.json_data

    def create_skill(self):

        if self.json_data.get('damage') is not None:
            self._clean_fields(['regeneration', 'level', 'school', 'is_verbal', 'is_somatic', 'is_material'])
            return Attack()
        elif self.json_data.get('regeneration') is not None:
            self._clean_fields(['damage', 'attack_range', 'attack_dices', 'level', 'school', 'is_verbal', 'is_somatic', 'is_material'])
            return Heal()
        elif self.json_data.get('school') is not None:
            self._clean_fields(['regeneration', 'damage', 'attack_range', 'attack_dices'])
            return Spell()
        else:
            self._clean_fields(['regeneration', 'level', 'school', 'duration', 'is_verbal', 'is_somatic', 'is_material', 'damage', 'attack_range', 'attack_dices'])
            return Skill()


class Skill(mongoengine.Document):
    def __str__(self):
        return 'Generic Skill'

    meta = {'collection': 'mop_skills','allow_inheritance': True}

    name = fields.StringField(required=True)
    usage_type = fields.StringField(required=True)
    description = fields.StringField(required=True)
    attack_bonus = fields.IntField()
    depends_on_skills = fields.ListField(fields.ReferenceField('Skill'))
    attack_multiplier = fields.StringField()
    defense_multiplier = fields.StringField()
    type = fields.StringField()

class Proficiency(Skill):
    bonus = fields.IntField()


class Attack(Skill):
    def __str__(self):
        return 'Attack'
    damage = fields.IntField()
    duration = fields.IntField()
    attack_range = fields.IntField()
    attack_dices = fields.ListField(fields.StringField())

class Heal(Skill):
    def __str__(self):
        return 'Heal'
    duration = fields.IntField()
    regeneration = fields.IntField()

class Spell(Skill):
    def __str__(self):
        return 'Spell'

    level = fields.IntField()
    school = fields.StringField()
    duration = fields.IntField()
    is_verbal = fields.BooleanField()
    is_somatic = fields.BooleanField()
    is_material = fields.BooleanField()
