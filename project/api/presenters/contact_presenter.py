import json
from django.http.response import HttpResponse
from api.presenters.interfaces.contact_presenter import ContactPresenter as ContactPresenterInterface


class ContactPresenter(ContactPresenterInterface):
    def __init__(self):
        self.content = []

    def show(self, contacts):
        for contact in contacts:
            self.content.append({
                'name': contact.name,
                'email': contact.email,
                'age': contact.age,
                'state': contact.state,
                'position': contact.position,
            })

    def response(self):
        return HttpResponse(
            content=json.dumps(self.content)
        )
 