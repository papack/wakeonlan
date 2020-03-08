from django.urls import path
from . import views

urlpatterns =[
    path('help', views.help, name="help"),
    path('about', views.about, name="about"),
]
