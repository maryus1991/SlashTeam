from contact.models import Contacts
from .serializers import ContactsSerializer
from rest_framework.generics import CreateAPIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class ContactsCreateAPIView(CreateAPIView):
    authentication_classes = []
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()


