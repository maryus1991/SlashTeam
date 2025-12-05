from django.urls import path
from .views import SiteMetaView, SiteDetailView, SendCsrfTokenView

app_label = 'site_setting'

urlpatterns = [
    path('/meta/', SiteMetaView.as_view(), name='site-meta'),
    path('/home/', SiteDetailView.as_view(), name='site-info'),
    path('/get-csrf-token/', SendCsrfTokenView.as_view(), name='get_csrf_token'),
]