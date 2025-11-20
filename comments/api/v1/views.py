from rest_framework.generics import ListAPIView
from.serializers import CommentsSerializer
from comments.models import Comments


class CommentsAPIView(ListAPIView):
    """for listing comments"""

    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
