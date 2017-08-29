from api.gateways.interfaces.segmentation_gateway import SegmentationGateway as SegmentationGatewayInterface
from api.models import Segmentation


class SegmentationGateway(SegmentationGatewayInterface):
    def get_by_id(self, segmentation_id):
        return Segmentation.objects.get(id=segmentation_id)
