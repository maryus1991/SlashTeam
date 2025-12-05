from contact.models import Contacts
from rest_framework import serializers

class ContactsSerializer(serializers.ModelSerializer):
    """create serializer for Contacts"""

    class Meta:
        model = Contacts
        fields = ('name', 'last_name', 'message', 'email')

