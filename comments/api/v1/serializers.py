from rest_framework import serializers
from comments.models import Comments
from drf_extra_fields.fields import Base64ImageField


class CommentsSerializer(serializers.ModelSerializer):
    """
    create serializer for comments
    """

    image = Base64ImageField(represent_in_base64=True)

    class Meta:
        model = Comments
        fields = [ 'name','is_active', 'comment', 'image']