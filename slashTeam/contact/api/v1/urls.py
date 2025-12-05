from django.urls import path
from .views import ContactsCreateAPIView

app_name = 'contact'

urlpatterns = [
    path('create/', ContactsCreateAPIView.as_view(), name='create'),
]