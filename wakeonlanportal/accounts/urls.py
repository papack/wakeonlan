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
    path('<str:name>/edit/', views.edit_user, name="edit_user"),
    path('<str:name>/deactivate/', views.deactivate_user, name="deactivate_user"),
    path('<str:name>/activate/', views.activate_user, name="activate_user"),
    path('<str:name>/make_admin/', views.make_admin, name="make_admin"),
    path('<str:name>/make_user/', views.make_user, name="make_user"),
    path('<str:name>/del/', views.del_user, name="del_user"),
    path('change_password/', views.change_password, name="change_password"),
]
