from django.shortcuts import render, HttpResponse

# Create your views here.

def my_log(request):
    return render(request, 'systemlog/log.html')

def systemlog(request):
    return render(request, 'systemlog/log.html')
