from django.urls import path
from . import views

urlpatterns =[
    path('', views.all_devices, name="all_devices"),
    path('new', views.new_device, name="new_device"),
    path('<slug:name>/edit', views.edit_device, name="edit_device"),
    path('<slug:name>/del', views.del_device, name="del_device"),
]
