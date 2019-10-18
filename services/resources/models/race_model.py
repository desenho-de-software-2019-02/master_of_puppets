from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongo', 27017)
db = client['mop']
race_collection = db['race']


class raceModel:
    def insert_new_race(data):
        new_element = {
            "name": data["name"],
            "description": data["description"],
            "restriction": data["restriction"],
            "exclusiveSkills": data["exclusiveSkills"]
        }

        id = race_collection.insert_one(new_element).inserted_id
        return "'{}'sucessfully added".format(id)

    def list_race():
        classes = []
        all_classes_db = race_collection.find()
        for Class in all_classes_db:

            info = {
                '_id': str(Class['_id']),
                'name': Class['name'],
                'description': Class['description'],
                'restriction': Class['restriction'],
                'exclusiveSkills': Class['exclusiveSkills'],

            }
            classes.append(info)

        if classes == []:
            return "there are no classes yet"
        return classes

    def delete_race_db(id):

        race_collection.delete_one({"_id": ObjectId(id)})
        return "'{}'sucessfully delete".format(id)

    def update_race_db(data):
        id = data["_id"]
        race_collection.update_one({'_id': ObjectId(id)}, {'$set':
                                                           {'name': data["name"],
                                                            "description": data["description"],
                                                            "restriction": data["restriction"],
                                                            "exclusiveSkills": data["exclusiveSkills"]}

                                                           })
        return data["name"]

    def get_race(id):
        result = race_collection.find_one({"_id": ObjectId(id)})
        return result
