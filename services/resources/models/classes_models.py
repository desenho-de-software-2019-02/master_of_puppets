from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongo', 27017)
db = client['mop']
classes_collection = db['mop_classes']

def create_new_class(data):
    new_element = {
        'name': data['name'],
        'description': data['description'],
        'exclusiveSkills': data['exclusiveSkills'],
        'effects': data['effects'],
        'restrictions': data['restrictions']
    }
    classes_collection.insert_one(new_element)

    return "'{}' sucessfully added".format(data['name'])

def verify_if_class_exists(ID):
    all_classes_db = classes_collection.find()

    for Class in all_classes_db:
        if Class['_id'] == ObjectId(ID):
            return True
    return False

def read_classes():
    classes = []
    all_classes_db = classes_collection.find() 
    for Class in all_classes_db:
        info = {
            '_id': Class['_id'],
            'name': Class['name'],
            'description': Class['description'],
            'effects': Class['effects'],
            'exclusiveSkills': Class['exclusiveSkills'],
            'restrictions': Class['restrictions']
        }
        classes.append(info) 
    
    if classes == []:
        return "there are no classes yet"
    return classes

def att_class(data):
    updated = {
        'name': data['name'],
        'description': data['description'],
        'effects': data['effects'],
        'exclusiveSkills': data['exclusiveSkills'],
        'restrictions': data['restrictions']
    }
    response = classes_collection.update({"name":data['old_name']}, {"$set": updated})
    if response['nModified'] == 1:
        return 'sucessfully updated'
    return "error"

def remove_class(data):
    response = classes_collection.remove({"_id": ObjectId(data['_id'])})
    if response['n'] == 1:
        return "{} sucessfully removed".format(data['_id'])
    return "error"

def info(data):
    all_classes_db = classes_collection.find()
    for Class in all_classes_db:
        if Class['name'] == data['name']:
            return Class
