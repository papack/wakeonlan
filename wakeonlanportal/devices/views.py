from django.shortcuts import render, HttpResponse

# Create your views here.

def my_devices(request):
    return render(request, 'devices/device.html')

def all_devices(request):
    return render(request, 'devices/device.html')

def new_device(request):
    return render(request, 'devices/new.html')
