from rest_framework import status, response, views
from rest_framework.permissions import IsAuthenticated

from site_setting.models import Site
from rest_framework.generics import RetrieveAPIView
from .serializers import SiteSerializer, SiteMetaSerializer
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from rest_framework.authentication import SessionAuthentication

@method_decorator(ensure_csrf_cookie, name='dispatch')
class SendCsrfTokenView(views.APIView):
    """
    send csrf token to front end for front validation
    """
    authentication_classes = (SessionAuthentication,)
    def get(self, request):
        return response.Response(
            {'X-CSRFTOKEN':request.META.get('CSRF_COOKIE') }
            , status=status.HTTP_200_OK)


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
