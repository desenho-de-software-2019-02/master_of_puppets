from json import dumps, loads
from models.campaign import Campaign
from flask_restplus import reqparse

class CampaignController:
    def __init__(self, request):
        self.request = request

    def new(self):

        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('gameMaster', required=True)
        parser.add_argument('players', action='append')
        parser.add_argument('characters', action='append')
        parser.add_argument('rules', action='append')
        parse_result = parser.parse_args(req=self.request)

        campaign = Campaign.from_json(dumps(parse_result)).save()

        return "{}".format(campaign.id)

    @staticmethod
    def list():
        list_of_campaigns = list(map(lambda campaign: loads(campaign.to_json()), Campaign.objects.all()))
        return list_of_campaigns

    @staticmethod
    def get_element_detail(identifier):
        return Campaign.objects.get(id=identifier).to_json()
    
    def edit(self, identifier):
        campaign = Campaign.objects.get(id=identifier)
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=False)
        parser.add_argument('gameMaster', required=False)
        parser.add_argument('players', required=False)
        parser.add_argument('characters', required=False)
        parser.add_argument('rules', required=False)
        parse_result = parser.parse_args(req=self.request)

        filtered_result = {k: v for k, v in parse_result.items() if v is not None}
        
        no_docs_updated = campaign.update(**filtered_result)

        if no_docs_updated == 1:
            new_campaign = Campaign.objects.get(id=identifier)
            return loads(new_campaign.to_json())
    
    @staticmethod
    def delete(id):
        target = Campaign.objects.get(id=id)
        target_data = loads(target.to_json())
        target.delete()

        return target_data