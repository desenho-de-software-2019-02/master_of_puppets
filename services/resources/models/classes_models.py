from pymongo import MongoClient

client = MongoClient('mongo', 27017)
db = client['mop']
classes_collection = db['mop_classes']

def create_new_class(data):
    new_element = {
        'name': data['name'],
        'info': data['info'],
        'effects': data['effects'],
        'skills': data['skills'],
        'restrictions': data['restrictions']
    }
    classes_collection.insert_one(new_element)

def verify_if_class_exists(data):
    all_classes_db = classes_collection.find()

    for Class in all_classes_db:
        if Class['name'] == data['name']:
            return True
    return False