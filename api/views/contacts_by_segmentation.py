import json
from django.views.generic import View
from api.presenters.contact_presenter import ContactPresenter
from api.gateways.contact_gateway import ContactGateway
from api.gateways.segmentation_gateway import SegmentationGateway
from api.usecases.search_contacts_by_segmentation import SearchContactsBySegmentation


class ContactsBySegmentation(View):
    def get(self, _, segmentation_id):
        presenter = ContactPresenter()

        SearchContactsBySegmentation(
            SegmentationGateway(),
            ContactGateway(),
            presenter
        ).execute(segmentation_id)

        return presenter.response()
