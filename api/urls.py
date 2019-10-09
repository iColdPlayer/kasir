from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('api/', views.ApiList.as_view(), name='ApiList'),
    path('api/<int:pk>/', views.ApiDetail.as_view(), name='ApiDetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)