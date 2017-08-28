import json
from api.models import Contact
from api.gateways.query_builder import QueryBuilder
from api.gateways.interfaces.contact_gateway import ContactGateway as ContactGatewayInterface


class ContactGateway(ContactGatewayInterface):
    @staticmethod
    def find_by_segmentation(segmentation):
        json_query = json.loads(segmentation.query)
        where = QueryBuilder(json_query).to_sql()
        
        query = f"select * from api_contact {where}"

        return list(Contact.objects.raw(query))
