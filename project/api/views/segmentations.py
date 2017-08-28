import json
from django.http.response import HttpResponse
from django.views.generic import View
from api.models import Segmentation
from api.structs.segmentation import Segmentation as SegmentationStruct


class Segmentations(View):
    def get(self, _, segmentation_id=None):
        if segmentation_id:
            segmentation = Segmentation.objects.get(id=segmentation_id)

            return HttpResponse(
                json.dumps(
                    SegmentationStruct(id=segmentation.id,
                                       query=segmentation.query).__dict__),
                content_type='application/json')
        else:
            segmentations = Segmentation.objects.all()
            return HttpResponse(
                json.dumps([SegmentationStruct(id=segmentation.id,
                                               query=segmentation.query).__dict__
                            for segmentation in segmentations]),
                content_type='application/json')

    def post(self, request):
        data = json.loads(request.body)
        Segmentation(**data).save()
        return HttpResponse(status=201)

    def put(self, request, segmentation_id):
        data = json.loads(request.body)
        Segmentation.objects.filter(id=segmentation_id).update(**data)
        return HttpResponse()

    def delete(self, _, segmentation_id):
        Segmentation.objects.filter(id=segmentation_id).delete()
        return HttpResponse()
