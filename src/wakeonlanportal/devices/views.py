from django.shortcuts import render, HttpResponse, redirect
from .models import Device
from .forms import NewDeviceForm
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from wakeonlan import send_magic_packet
from django.contrib import messages

@login_required
def wakeup_device(request, name):

    try:
        device = Device.objects.get(name=name)
    except ObjectDoesNotExist:
        return redirect('/')

    #Send the MagicPacet
    send_magic_packet(str(device.mac))

    messages.success(request, 'Magicpacket was sent to '+str(device)+' !')
    return redirect('/')

@login_required
def all_devices(request):
    devices = Device.objects.all().order_by('name')
    return render(request, 'devices/device.html', {'devices':devices})

@staff_member_required
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

@staff_member_required
def edit_device(request, name):

    try:
        device = Device.objects.get(name=name)
    except ObjectDoesNotExist:
        return redirect('/')

    if request.method == 'POST':
        form = NewDeviceForm(request.POST,instance=device)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'devices/edit.html', { 'form' : form, 'device' : device })

    else:

        form = NewDeviceForm(instance=device)
        return render(request, 'devices/edit.html', { 'form' : form, 'device' : device })


@staff_member_required
def del_device(request, name):

    try:
        device = Device.objects.get(name=name)
    except ObjectDoesNotExist:
        return redirect('/')

    device.delete()
    return redirect('/')
