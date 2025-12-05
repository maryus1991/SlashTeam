from rest_framework.generics import ListAPIView
from members.models import Members
from .serializers import MembersSerializer

class MembersListAPIView(ListAPIView):
    """
    api for return members list
    """

    queryset = Members.objects.all()
    serializer_class = MembersSerializer