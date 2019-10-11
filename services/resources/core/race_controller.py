from models.race_model import raceModel
class raceController:
    def create_race(data):
        #validar dados 
        return raceModel.insert_new_race(data)


    def get_race_list():
        return raceModel.list_race()

    def delete_race(data):
        id  = data["_id"]
        return raceModel.delete_race_db(id)


    def update_race(data):
        return raceModel.update_race_db(data)

    def read_race(id):
        
        result = raceModel.get_race(id)
        result["_id"]= str(result["_id"])
        return result