import json

from django.http.response import HttpResponse
from django.views.generic import View


class ContactsBySegmentation(View):
    def get(self, request, segmentation_id):
        pass
