from django.test import TestCase

from api.gateways.segmentation_gateway import SegmentationGateway
from api.models import Segmentation


class SegmentationGatewayTests(TestCase):
    def setUp(self):
        self.gateway = SegmentationGateway()

    def test_get_segmentation_by_id(self):
        segmentation = Segmentation.objects.create()

        segmentation_founded = self.gateway.get_by_id(segmentation.id)

        self.assertEqual(segmentation, segmentation_founded)
