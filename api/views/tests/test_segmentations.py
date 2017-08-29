import json
from django.test import TestCase, Client
from api.models import Segmentation


class SegmentationsTests(TestCase):
    def setUp(self):
        self.request = Client()

    def test_get_segmentation_id(self):
        segmentation = Segmentation.objects.create(query="{}")

        response = self.request.get(f'/api/v1/segmentations/{segmentation.id}/')

        self.assertEqual(200, response.status_code)
        content = json.loads(response.content)
        self.assertEqual(segmentation.id, content['id'])
        self.assertEqual(segmentation.query, content['query'])

    def test_get_all_segmentations(self):
        segmentation_1 = Segmentation.objects.create(query="{}")
        segmentation_2 = Segmentation.objects.create(query="[{}]")

        response = self.request.get('/api/v1/segmentations/')

        self.assertEqual(200, response.status_code)
        content = json.loads(response.content)
        self.assertEqual(2, len(content))
        self.assertEqual(segmentation_1.id, content[0]['id'])
        self.assertEqual(segmentation_1.query, content[0]['query'])
        self.assertEqual(segmentation_2.id, content[1]['id'])
        self.assertEqual(segmentation_2.query, content[1]['query'])
    
    def test_create_segmentation(self):
        segmentation_query = {
            'column': 'age',
            'operator': '>=',
            'value': 35,
            'type': 'numeric' 
        }

        response = self.request.post(
            '/api/v1/segmentations/',
            json.dumps({'query': segmentation_query}),
            content_type='application/json'
        )

        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(json.loads(response.content)['id'])
        segmentation_created = Segmentation.objects.all()[0] 
        self.assertIsNotNone(segmentation_created.id)
        self.assertEqual(str(segmentation_query), segmentation_created.query)

    def test_update_segmentation(self):
        segmentation = Segmentation.objects.create(
            query="{'column': 'age': 'operator': '>=', 'value': 35, 'type': 'numeric'}")

        response = self.request.put(
            f'/api/v1/segmentations/{segmentation.id}/',
            json.dumps({'query': {'column': 'age', 'operator': '>=', 'value': 30, 'type': 'numeric'}}),
            content_type='application/json'
        )

        self.assertEqual(200, response.status_code)
        self.assertEqual(
            "{'column': 'age', 'operator': '>=', 'value': 30, 'type': 'numeric'}",
            Segmentation.objects.get(id=segmentation.id).query)

    def test_delete_segmentation(self):
        segmentation_1 = Segmentation.objects.create()
        segmentation_2 = Segmentation.objects.create()

        response = self.request.delete(f'/api/v1/segmentations/{segmentation_1.id}/')

        self.assertEqual(200, response.status_code)
        self.assertEqual(0, Segmentation.objects.filter(id=segmentation_1.id).count())
