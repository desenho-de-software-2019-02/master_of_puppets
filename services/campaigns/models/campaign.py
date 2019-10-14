from pymongo import MongoClient
from flask_api import status
# from bson import ObjectID


client = MongoClient('mongo', 27017)
db = client['mop']
campaign_collection = db['mop_campaign']

class campaignModel:

    def create_new_campaign(data):
        new_element = {
            "gameMaster": data["gameMaster"],
            "players": data["players"],
            "characters": data["characters"],
            "rules": data["rules"],
            "session": data["session"],
            "date_initial": data["session"]
        }   
        print(campaign_collection.insert_one(new_element))
        return status.HTTP_201_CREATED
        return status.HTTP_400_BAD_REQUEST

    def list_campaigns():
        campaigns = []
        all_campaigns = campaign_collection.find() 
        for campaign in all_campaigns:
            element = {
                "gameMaster": campaign["gameMaster"],
                "players": campaign["players"],
                "characters": campaign["characters"],
                "rules": campaign["rules"],
                "session": campaign["session"],
                "date_initial": campaign["session"]
            }
            campaigns.append(element)         
        return campaigns, status.HTTP_200_OK
    #WIP
    # def delete_campaign(id):
    #     campaign_collection.delete_one({'_id': ObjectId(id)})

    def gameMaster_campaigns(name):
        all_campaigns = campaign_collection.find()
        campaign_gameMaster = []
        for campaign in all_campaign:
            if campaign['gameMaster'] == name:
                campaign_gameMaster.append(campaign)
        if campaign_gameMaster:
            return "This master has no campaigns"
        return campaign_gameMaster
