from django.urls import path
from . import views

urlpatterns =[
    path('', views.my_devices, name="my_devices"),
    path('all', views.all_devices, name="all_devices"),
    path('new', views.new_device, name="new_device"),
]
