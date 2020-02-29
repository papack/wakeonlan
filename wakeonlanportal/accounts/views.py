from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect('login')

def list(request):
    return render(request, 'accounts/list.html')

def new_user(request):
    return render(request, 'accounts/new.html')

def change_password(request):
    return render(request, 'accounts/password.html')

def edit(request):
    return render(request, 'accounts/edit.html')
