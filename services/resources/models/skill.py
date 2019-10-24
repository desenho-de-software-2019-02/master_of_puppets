import mongoengine
import mongoengine.fields as fields


class Skill(mongoengine.Document):
    meta = {'collection': 'mop_skills','allow_inheritance': True}

    name = fields.StringField(required=True)
    usage_type = fields.StringField(required=True)
    description = fields.StringField(required=True)
    depends_on_skills = fields.ListField(fields.ReferenceField('Skill'))
    attack = fields.StringField()


class Proficiency(Skill):
    bonus = fields.IntField()


class Attack(Skill):
    attack_bonus = fields.IntField()
    attack_range = fields.IntField()
    attack_dices = fields.ListField(fields.ReferenceField('Dice'))


class Spell(Attack):
    level = fields.IntField()
    school = fields.StringField()
    casting_time = fields.IntField()
    duration = fields.IntField()
    is_verbal = fields.BooleanField()
    is_somatic = fields.BooleanField()
    is_material = fields.BooleanField()
