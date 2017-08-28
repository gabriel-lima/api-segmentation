import json
from django.test import TestCase, Client
from api.models import Contact, Segmentation


class ContactsBySegmentationTests(TestCase):
    def setUp(self):
        self.request = Client()

    def test_get_contacts_by_segmentation_id(self):
        contact_out_by_state = Contact.objects.create(name="Name 2", email="name2@email.com", age=30, state="RS", position="Software Engineer")
        contact_out_by_age = Contact.objects.create(name="Name 3", email="name3@email.com", age=30, state="SC", position="Software Engineer")
        contact_in = Contact.objects.create(name="Name 1", email="name1@email.com", age=31, state="SC", position="Software Engineer")
        segmentation = Segmentation.objects.create(
            query="""{
                "and": [
                    {"column": "state", "operator": "=", "value": "SC", "type": "text"}, 
                    {"column": "age", "operator": ">", "value": 30, "type": "numeric"}
                ]
            }"""
        )

        response = self.request.get(f"/api/v1/segmentations/{segmentation.id}/contacts/")

        self.assertEqual(200, response.status_code)
        content = json.loads(response.content)
        self.assertEqual(1, len(content))
        self.assertEqual(contact_in.name, content[0]['name'])
        self.assertEqual(contact_in.email, content[0]['email'])
        self.assertEqual(contact_in.age, content[0]['age'])
        self.assertEqual(contact_in.state, content[0]['state'])
        self.assertEqual(contact_in.position, content[0]['position'])
