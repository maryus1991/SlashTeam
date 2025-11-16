from service.models import Service
from rest_framework import serializers


class MemberSerializer(serializers.ModelSerializer):
    """create serializer for Members"""
    class Meta:
        model = Service
        fields = '__all__'