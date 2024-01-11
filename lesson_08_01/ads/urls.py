from django.urls import path
from .views import index, ad_list

urlpatterns = [
    path('<int:pk>/', index), # /1 /2 /101241
    path('', ad_list)
]

