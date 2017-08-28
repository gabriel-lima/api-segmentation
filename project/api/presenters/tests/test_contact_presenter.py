import json
from django.http.response import HttpResponse
from api.presenters.interfaces.contact_presenter import ContactPresenter as ContactPresenterInterface


from unittest import TestCase
from api.presenters.contact_presenter import ContactPresenter
from api.models import Contact


class ContactPresenterTests(TestCase):
    def setUp(self):
        self.presenter = ContactPresenter()

    def assertContact(self, contact_expected, contact_founded):
        self.assertEqual(contact_expected.name, contact_founded['name'])
        self.assertEqual(contact_expected.email, contact_founded['email'])
        self.assertEqual(contact_expected.age, contact_founded['age'])
        self.assertEqual(contact_expected.state, contact_founded['state'])
        self.assertEqual(contact_expected.position, contact_founded['position'])

    def test_show_contacts(self):
        contact_1 = Contact.objects.create(name="Contact 1", email="2@email.com", age=15, state="RS", position="Software Engineer I")
        contact_2 = Contact.objects.create(name="Contact 2", email="1@email.com", age=30, state="SC", position="Software Engineer II")
        self.presenter.show([contact_1, contact_2])

        response = self.presenter.response()

        self.assertEqual(200, response.status_code)
        content = json.loads(response.content)
        self.assertEqual(2, len(content))
        self.assertContact(contact_1, content[0])
        self.assertContact(contact_2, content[1])
