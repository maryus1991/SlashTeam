from about_team.models import About
from rest_framework.generics import RetrieveAPIView
from .serializers import AboutTeamSerializer

class AboutListAPIView(RetrieveAPIView):
    """
    api for return about team description
    """

    serializer_class = AboutTeamSerializer

    def get_object(self):
        queryset = About.objects.first()
        return queryset
