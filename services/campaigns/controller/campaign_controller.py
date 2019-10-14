from models.campaign import campaignModel

class campaignController:
    def create_campaign(data):

        # Validar os dados do character
        return campaignModel.create_new_campaign(data) 

    def get_campaigns():
        return campaignModel.list_campaigns()

    def get_campaign_master(gameMaster):
        list_campaign = gameMaster_campaigns(gameMaster)
        if list_campaign:
            return list_campaign
        return 'This master no have campaign'

    def delete_campaign(data):
        id = data['_id']
        return campaignModel.delete_campaign(id)

