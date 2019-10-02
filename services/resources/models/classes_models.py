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

    return "'{}' sucessfully added".format(data['name'])

def verify_if_class_exists(data):
    all_classes_db = classes_collection.find()

    for Class in all_classes_db:
        if Class['name'] == data['name']:
            return True
    return False

def read_classes():
    classes = []
    all_classes_db = classes_collection.find() 
    for Class in all_classes_db:
        info = {
            'name': Class['name'],
            'info': Class['info'],
            'effects': Class['effects'],
            'skills': Class['skills'],
            'restrictions': Class['restrictions']
        }
        classes.append(info) 
    
    if classes == []:
        return "there are no classes yet"
    return classes

def remove_class(data):
    response = classes_collection.remove({"name": data['name']})
    if response['n'] == 1:
        return "{} sucessfully removed".format(data['name'])
    return "error"
