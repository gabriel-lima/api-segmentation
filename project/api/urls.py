from django.conf.urls import url

from api.views.contacts import Contacts
from api.views.segmentations import Segmentations
from api.views.contacts_by_segmentation import ContactsBySegmentation


urlpatterns = [
    url(r'^v1/contacts/(?P<contact_id>\d+)/$', Contacts.as_view()),
    url(r'^v1/segmentations/(?P<segmentation_id>\d+)/$', Segmentations.as_view()),
    url(r'^v1/segmentations/(?P<segmentation_id>\d+)/contacts/$', ContactsBySegmentation.as_view()),
]
