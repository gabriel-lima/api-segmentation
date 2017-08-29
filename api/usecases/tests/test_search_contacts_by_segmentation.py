from unittest import TestCase
from unittest.mock import create_autospec

from api.usecases.search_contacts_by_segmentation import SearchContactsBySegmentation
from api.gateways.interfaces.segmentation_gateway import SegmentationGateway
from api.gateways.interfaces.contact_gateway import ContactGateway
from api.presenters.interfaces.contact_presenter import ContactPresenter
from api.structs.segmentation import Segmentation
from api.structs.contact import Contact


SEGMENTATION_ID = 123


class SearchContactsBySegmentationTests(TestCase):
    def setUp(self):
        self.segmentation_gateway = create_autospec(SegmentationGateway)
        self.contact_gateway = create_autospec(ContactGateway)
        self.contact_presenter = create_autospec(ContactPresenter)

        self.usecase = SearchContactsBySegmentation(
            self.segmentation_gateway,
            self.contact_gateway,
            self.contact_presenter
        )

    def test_get_segmentation_by_id(self):
        self.usecase.execute(SEGMENTATION_ID)

        self.segmentation_gateway.get_by_id.assert_called_once_with(SEGMENTATION_ID)

    def test_find_contacts_by_segmentation(self):
        segmentation = Segmentation()
        self.segmentation_gateway.get_by_id.return_value = segmentation

        self.usecase.execute(SEGMENTATION_ID)

        self.contact_gateway.find_by_segmentation.assert_called_once_with(segmentation)

    def test_show_contacts_found(self):
        contacts = [Contact()]
        self.contact_gateway.find_by_segmentation.return_value = contacts

        self.usecase.execute(SEGMENTATION_ID)

        self.contact_presenter.show.assert_called_once_with(contacts)
