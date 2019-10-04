from pymongo import MongoClient

client = MongoClient('mongo', 27017)
db = client['mop']
race_collection = db['race']

def insert_new_race(data):
    new_element = {
        "name": data["name"],
        "description":data["description"],
        "restriction":data["restriction"],
        "exclusiveSkills":data["exclusiveSkills"]
    }
    
    race_collection.insert_one(new_element)
    return "'{}'sucessfully added".format(data["name"])

def read_race():
    classes = []
    all_classes_db = race_collection.find() 
    for Class in all_classes_db:
        info = {
            'name': Class['name'],
            'description': Class['description'],
            'restriction': Class['restriction'],
            'exclusiveSkills': Class['exclusiveSkills'],
            
        }
        classes.append(info) 
    
    if classes == []:
        return "there are no classes yet"
    return classes