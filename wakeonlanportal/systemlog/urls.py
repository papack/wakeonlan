from django.urls import path
from . import views

urlpatterns =[
    path('', views.my_log, name="my_log"),
    path('all', views.systemlog, name="systemlog"),
]
