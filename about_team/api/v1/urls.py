from django.urls import path
from .views import AboutListAPIView

app_name = 'about'

urlpatterns = [
    path('', AboutListAPIView.as_view(), name='list'),
]