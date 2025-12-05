from drf_extra_fields.fields import Base64ImageField
from site_setting.models import Site
from rest_framework import serializers

class SiteSerializer(serializers.ModelSerializer):
    """
    for return sites information
    """

    image = Base64ImageField(represent_in_base64=True)

    class Meta:
        model = Site
        fields = ('about_work_keywords', 'description_home', 'image')


class SiteMetaSerializer(serializers.ModelSerializer):
    """
    for return sites meta information
    """
    class Meta:
        model = Site
        fields = ('keywords_meta_tag', 'description_meta_tag', 'author_meta_tag')