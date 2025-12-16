from rest_framework import serializers
from about_team.models import About


class AboutTeamSerializer(serializers.Serializer):
    """
    create serializer for AboutTeam model
    """
    class Meta:
        model = About
        fields = '__all__'