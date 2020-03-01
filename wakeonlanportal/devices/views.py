from django.shortcuts import render, HttpResponse
from .models import Device

def all_devices(request):
    devices = Device.objects.all().order_by('name')
    return render(request, 'devices/device.html', {'devices':devices})

def new_device(request):
    return render(request, 'devices/new.html')
