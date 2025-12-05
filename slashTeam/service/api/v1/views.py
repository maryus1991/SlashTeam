from service.models import  Service
from rest_framework.generics import ListAPIView
from .serializers import MemberSerializer


class ServiceAPIListView(ListAPIView):
    """
    for return services list
    """
    queryset = Service.objects.all()
    serializer_class = MemberSerializer