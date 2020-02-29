from django.shortcuts import render, HttpResponse

# Create your views here.

def about(request):
    return render(request, 'information/about.html')

def help(request):
    return render(request, 'information/help.html')
