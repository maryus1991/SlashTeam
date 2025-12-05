from contact.models import Contacts
from .serializers import ContactsSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.authentication import SessionAuthentication
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator


@method_decorator(csrf_protect, name='dispatch')
class ContactsCreateAPIView(CreateAPIView):

    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    authentication_classes = [SessionAuthentication]

