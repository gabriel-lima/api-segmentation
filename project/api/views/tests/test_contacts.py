import json
from django.test import TestCase, Client
from api.models import Contact


class ContactsTests(TestCase):
    def setUp(self):
        self.request = Client()

    def assertContact(self, contact_expected, contact_founded):
        self.assertEqual(contact_expected.name, contact_founded['name'])
        self.assertEqual(contact_expected.email, contact_founded['email'])
        self.assertEqual(contact_expected.age, contact_founded['age'])
        self.assertEqual(contact_expected.state, contact_founded['state'])
        self.assertEqual(contact_expected.position, contact_founded['position']) 
    
    def test_get_contact(self):
        contact = Contact.objects.create(name='Name 1', email='1@email.com', age=25, state='SC', position='Developer')

        response = self.request.get(f'/api/v1/contacts/{contact.id}/')

        self.assertEqual(200, response.status_code)
        content = json.loads(response.content)
        self.assertContact(contact, content)
    
    def test_get_all_contacts(self):
        contact_1 = Contact.objects.create(name='Name 1', email='1@email.com', age=25, state='SC', position='Developer')
        contact_2 = Contact.objects.create(name='Name 2', email='2@email.com', age=25, state='SC', position='Developer')

        response = self.request.get(f'/api/v1/contacts/')

        self.assertEqual(200, response.status_code)
        content = json.loads(response.content)
        self.assertEqual(2, len(content))
        self.assertContact(contact_1, content[0])
        self.assertContact(contact_2, content[1])

    def test_create_contact(self):
        response = self.request.post(
            '/api/v1/contacts/',
            json.dumps({'name': 'Contact 1', 'email': '1@email.com', 'age': 30, 'state': 'SC', 'position': 'Software Engineer'}),
            content_type='application/json'
        )

        self.assertEqual(201, response.status_code)
        contact_created = Contact.objects.all()[0] 
        self.assertEqual('Contact 1', contact_created.name)
        self.assertEqual('1@email.com', contact_created.email)
        self.assertEqual(30, contact_created.age)
        self.assertEqual('SC', contact_created.state)
        self.assertEqual('Software Engineer', contact_created.position)

    def test_update_contact(self):
        contact = Contact.objects.create(name='Name 1', email='1@email.com', age=25, state='SC', position='Software Engineer')

        response = self.request.put(
            f'/api/v1/contacts/{contact.id}/',
            json.dumps({'name': 'Name 1', 'email': '1@email.com', 'age': 30, 'state': 'SC', 'position': 'Software Engineer'}),
            content_type='application/json'
        )

        self.assertEqual(200, response.status_code)
        self.assertEqual(30, Contact.objects.get(id=contact.id).age)

    def test_delete_contact(self):
        other_contact = Contact.objects.create(name='Name 1', email='1@email.com', age=25, state='SC', position='Software Engineer')
        contact = Contact.objects.create(name='Name 1', email='1@email.com', age=25, state='SC', position='Software Engineer')

        response = self.request.delete(f'/api/v1/contacts/{contact.id}/')

        self.assertEqual(200, response.status_code)
        self.assertEqual(0, Contact.objects.filter(id=contact.id).count())
