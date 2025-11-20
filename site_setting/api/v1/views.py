from site_setting.models import Site
from rest_framework.generics import RetrieveAPIView
from .serializers import SiteSerializer, SiteMetaSerializer


class SiteMetaView(RetrieveAPIView):
    """
    for return site meta information
    """

    queryset = Site.objects.all()
    serializer_class = SiteMetaSerializer

    def get_object(self):
        return self.queryset.first()

class SiteDetailView(RetrieveAPIView):
    """
    for return site detail information
    """
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

    def get_object(self):
        return self.queryset.first()
