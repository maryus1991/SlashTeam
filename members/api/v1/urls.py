from django.urls import path
from .views import MembersListAPIView

app_name = 'members'

urlpatterns = [
    path('', MembersListAPIView.as_view(), name='list'),
]