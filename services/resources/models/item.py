from pymongo import MongoClient

client = MongoClient('mongo', 27017)
db = client['mop']
items_collection = db['mop_items']


def insert_new_item(data):
    new_element = {
        "name": data["name"],
        "description": data["description"],
        "price": data["price"],
        "weight": data["weight"]
    }

    result = items_collection.insert_one(new_element)
    return str(result.inserted_id)


"""
class ItemModel:
    def __init__(self, name, description, price, weight):
        # self.__name = name
        # self.__description = description
        # self.__price = price
        # self.__weight = weight
        self.name = name
        self.description = description
        self.price = price
        self.weight = weight

    def update(self):
        changes = {
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'weight': self.weight
            # 'name': self.get_name(),
            # 'description': self.get_description(),
            # 'price': self.get_price(),
            # 'weight': self.get_weight()
        }

        updated = items_collection.update_one(
            {'name': self.get_name},
            changes
        )

        if updated is None:
            return False

        return True

        # el = items_collection.find_one({"name": self.get_name()})
        # el = {
        #     '_id': el._id
        # }

        # if el is not None:
        #     resp = items_collection.find_one_and_update(
        #         {'name': self.get_name()})
        #     return resp is not None

        # return False

    def create(self, data):
        new_element = {
            "name": data["name"],
            "description": data["description"],
            "price": data["price"],
            "weight": data["weight"]
        }

        ret = items_collection.insert_one(new_element)

        if ret is None:
            return False

        return True

    def delete(self):
        deleted = items_collection.delete_one({'name': self.name})

        if deleted.deleted_count != 1:
            return False
        return True

    # def save(self):
    #     new_element = {
    #         "name": self.__name,
    #         "description": self.__description,
    #         "price": self.__price,
    #         "weight": self.__weight
    #     }

    #     items_collection.insert_one(new_element)


class ArmorModel(ItemModel):
    pass


class WeaponModel(ItemModel):
    pass


class EffectItemModel(ItemModel):
    pass
"""