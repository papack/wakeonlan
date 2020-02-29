from django.shortcuts import render, HttpResponse

# Create your views here.

def systemlog(request):
    return render(request, 'systemlog/log.html')
