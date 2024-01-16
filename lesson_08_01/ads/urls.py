from django.urls import path
from .views import index, ad_list, AdCreateView

urlpatterns = [
    path('<int:pk>/fafawdawdawdawdawdafsz', index, name='ad_detail'), # /1 /2 /101241
    path('create/', AdCreateView.as_view(), name='create_ad'),
    path('', ad_list)
]

