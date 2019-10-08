import mongoengine
import mongoengine.fields as fields

mongoengine.connect('mop', host='mongo:27017')


class Item(mongoengine.Document):
    meta = {'collection': 'mop_items', 'allow_inheritance': True}

    name = fields.StringField(required=True)
    description = fields.StringField(required=True)
    price = fields.DecimalField(required=True, min_value=0, precision=2)
    weight = fields.DecimalField(required=True, min_value=0, precision=2)


class Armor(Item):
    weapon_type = fields.StringField()
    # 32bit integer field, for 64 use LongField()
    armor_class_mod = fields.IntField()
    armor_class_max = fields.IntField()


class Weapon(Item):
    dmg_dice = fields.ReferenceField('Dice')
    weapon_type = fields.StringField()


class EffectItem(Item):
    # only differs from Item on methods
    pass
