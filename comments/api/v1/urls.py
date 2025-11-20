from django.urls import path
from .views import CommentsAPIView

app_name = 'comments'

urlpatterns = [
    path('', CommentsAPIView.as_view(), name='list'),
]