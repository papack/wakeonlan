from django.urls import path
from . import views

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . forms import CustomAuthForm

urlpatterns =[
    path('login/', LoginView.as_view(template_name='accounts/login.html',authentication_form=CustomAuthForm), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('list_user/', views.list, name="list_user"),
    path('new/', views.new_user, name="new_user"),
    path('edit_user/', views.edit, name="edit_user"),
    path('change_password/', views.change_password, name="change_password"),
]
