from django.urls import path
from .views import SiteMetaView, SiteDetailView

app_label = 'site_setting'

urlpatterns = [
    path('/meta/', SiteMetaView.as_view(), name='site-meta'),
    path('/home/', SiteDetailView.as_view(), name='site-info'),
]