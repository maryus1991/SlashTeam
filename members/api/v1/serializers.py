from rest_framework import serializers
from members.models import Members
from drf_extra_fields.fields import Base64ImageField



class MembersSerializer(serializers.ModelSerializer):
    """create serializer for Members"""

    photo = Base64ImageField(represent_in_base64=True)

    class Meta:
        model = Members
        fields = ('id', 'name', 'skills', 'website', 'telegram', 'whatsapp', 'photo')
