from unittest.mock import create_autospec, patch

from django.test import TestCase

from api.models import Segmentation, Contact
from api.gateways.contact_gateway import ContactGateway
from api.gateways.query_builder import QueryBuilder


class ContactGatewayTests(TestCase):
    @patch('api.gateways.contact_gateway.QueryBuilder')
    def test_find_contacts_by_query_segmentation(self, query_builder):
        query_builder.return_value.to_sql.return_value = "where state = \"SC\" and age > 30"
        segmentation = Segmentation()
        contact_out_by_state = Contact.objects.create(name="Name 2", email="name2@email.com", age=30, state="RS", position="Software Engineer")
        contact_out_by_age = Contact.objects.create(name="Name 3", email="name3@email.com", age=30, state="SC", position="Software Engineer")
        contact_in = Contact.objects.create(name="Name 1", email="name1@email.com", age=31, state="SC", position="Software Engineer")        

        contacts = ContactGateway.find_by_segmentation(segmentation)

        self.assertEqual(1, len(contacts))
        self.assertEqual(contact_in, contacts[0])
