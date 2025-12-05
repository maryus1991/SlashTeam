from django.urls import path
from .views import ServiceAPIListView

app_name = 'service'

urlpatterns = [
    path('', ServiceAPIListView.as_view(), name='list'),
]