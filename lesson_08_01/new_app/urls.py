from .views import post_detail
from django.urls import path

urlpatterns = [
    path('<int:pk>/', post_detail, name='post_detail')
]

