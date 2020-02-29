from django.urls import path
from . import views

urlpatterns =[
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('activate', views.activate, name="initial_activate"),
    path('new', views.new_user, name="new_user"),
    path('edit_user', views.edit, name="edit_user"),
    path('change_password', views.change_password, name="change_password"),
]
