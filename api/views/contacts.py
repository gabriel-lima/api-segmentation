import json
from django.http.response import HttpResponse
from django.views.generic import View
from api.models import Contact
from api.structs.contact import Contact as ContactStruct


class Contacts(View):
    def get(self, _, contact_id=None):
        if contact_id:
            contact = Contact.objects.get(id=contact_id)

            return HttpResponse(
                json.dumps(
                    ContactStruct(
                        name=contact.name, 
                        email=contact.email, 
                        age=contact.age, 
                        state=contact.state, 
                        position=contact.position).__dict__),
                content_type='application/json')
        else:
            contacts = Contact.objects.all()
            return HttpResponse(
                json.dumps(
                    [ContactStruct(
                        name=contact.name, 
                        email=contact.email, 
                        age=contact.age, 
                        state=contact.state, 
                        position=contact.position).__dict__ for contact in contacts]),
                content_type='application/json')
    
    def post(self, request):
        data = json.loads(request.body)
        Contact(**data).save()
        return HttpResponse(status=201)

    def put(self, request, contact_id):
        data = json.loads(request.body)
        Contact.objects.filter(id=contact_id).update(**data)
        return HttpResponse()

    def delete(self, r_, contact_id):
        Contact.objects.filter(id=contact_id).delete()
        return HttpResponse()
