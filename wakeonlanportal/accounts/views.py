from django.shortcuts import render, HttpResponse, redirect


def list(request):
    return render(request, 'accounts/list.html')

def new_user(request):
    return render(request, 'accounts/new.html')

def change_password(request):
    return render(request, 'accounts/password.html')

def edit(request):
    return render(request, 'accounts/edit.html')
