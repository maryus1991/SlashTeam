from contact.models import Contacts
from .serializers import ContactsSerializer
from rest_framework.generics import CreateAPIView

class ContactsCreateAPIView(CreateAPIView):
    """
    for create new contact
    """

    serializer_class = ContactsSerializer
    model = Contacts