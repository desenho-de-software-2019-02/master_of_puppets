from models.item import insert_new_item


def validate_item_json(data):
    return insert_new_item(data)