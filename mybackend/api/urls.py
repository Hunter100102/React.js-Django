from django.urls import path
from .views import endpoint1, endpoint2

urlpatterns = [
    path('endpoint1/', endpoint1, name='endpoint1'),
    path('endpoint2/', endpoint2, name='endpoint2'),
]
