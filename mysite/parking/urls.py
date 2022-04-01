from django.urls import path
from . import views



app_name = 'parking'

urlpatterns = [
    path('',views.parking_request , name='parking_request' ),
]