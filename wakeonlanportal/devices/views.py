from django.shortcuts import render, HttpResponse, redirect
from .models import Device
from .forms import NewDeviceForm

def all_devices(request):
    devices = Device.objects.all().order_by('name')
    return render(request, 'devices/device.html', {'devices':devices})

def new_device(request):

    if request.method == 'POST':
        form = NewDeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'devices/new.html', { 'form' : form })

    else:
        form = NewDeviceForm()
        return render(request, 'devices/new.html', { 'form' : form })
