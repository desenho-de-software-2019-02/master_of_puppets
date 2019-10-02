from pymongo import MongoClient

client = MongoClient('mongo', 27017)
db = client['mop']
items_collection = db['mop_items']


# def insert_new_item(data):
#     new_element = {
#         "name": data["name"],
#         "description": data["description"],
#         "price": data["price"],
#         "weight": data["weight"]
#     }

#     items_collection.insert_one(new_element)


class ItemModel:
    def __init__(self, name, description, price, weigth):
        # self.__name = name
        # self.__description = description
        # self.__price = price
        # self.__weigth = weigth
        self.name = name
        self.description = description
        self.price = price
        self.weigth = weigth

    # def get_name(self):
    #     return self.__name

    # def get_description(self):
    #     return self.__description

    # def get_price(self):
    #     return self.__price

    # def get_weigth(self):
    #     return self.__weigth

    # def set_name(self, name):
    #     pass

    # def set_description(self, description):
    #     pass

    # def set_price(self, price):
    #     pass

    # def set_weigth(self, weigth):
    #     pass

    def update(self):
        changes = {
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'weigth': self.weigth
            # 'name': self.get_name(),
            # 'description': self.get_description(),
            # 'price': self.get_price(),
            # 'weigth': self.get_weigth()
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
    #         "weight": self.__weigth
    #     }

    #     items_collection.insert_one(new_element)


class ArmorModel(ItemModel):
    pass


class WeaponModel(ItemModel):
    pass


class EffectItemModel(ItemModel):
    pass
