from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Account")

def login(request):
    return render(request, 'accounts/login.html')
