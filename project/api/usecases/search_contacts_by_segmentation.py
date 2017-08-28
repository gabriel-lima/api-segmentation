class SearchContactsBySegmentation(object):
    def __init__(self, segmentation_gateway, contact_gateway, contacts_presenter):
        self.segmentation_gateway = segmentation_gateway 
        self.contact_gateway = contact_gateway
        self.contacts_presenter = contacts_presenter

    def execute(self, segmentation_id):
        segmentation = self.segmentation_gateway.get_by_id(segmentation_id)

        contacts = self.contact_gateway.find_by_segmentation(segmentation)

        self.contacts_presenter.show(contacts)
