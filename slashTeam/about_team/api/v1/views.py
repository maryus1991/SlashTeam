from about_team.models import About
from rest_framework.generics import ListAPIView
from .serializers import AboutTeamSerializer

class AboutListAPIView(ListAPIView):
    """
    api for return about team description
    """

    serializer_class = AboutTeamSerializer
    queryset = About.objects.all()
