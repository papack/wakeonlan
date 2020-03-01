from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .forms import NewUserForm

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages


def list(request):
    return render(request, 'accounts/list.html')


@staff_member_required
def list(request):
    user = User.objects.all().order_by('username')
    return render(request, 'accounts/list.html', {'users':user})

@staff_member_required
def new_user(request):

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("list_user"))
        else:
            return render(request, 'accounts/new.html', { 'form' : form })

    else:
        form = NewUserForm()
        return render(request, 'accounts/new.html', { 'form' : form })

def change_password(request):
    return render(request, 'accounts/password.html')

def edit(request):
    return render(request, 'accounts/edit.html')


@staff_member_required
def edit_user(request, name):

    try:
        u = User.objects.get(username=name)
    except ObjectDoesNotExist:
        return redirect(reverse("list_user"))

    if request.method == 'POST':
        form = NewUserForm(request.POST,instance=u)
        if form.is_valid():
            form.save()
            return redirect(reverse("list_user"))
        else:
            return render(request, 'accounts/edit.html', { 'form' : form, 'user' : u })

    else:

        form = NewUserForm(instance=u)
        return render(request, 'accounts/edit.html', { 'form' : form, 'user' : u })

@staff_member_required
def del_user(request, name):

    try:
        u = User.objects.get(username=name)
    except ObjectDoesNotExist:
        return redirect(reverse("list_user"))

    u.delete()
    return redirect(reverse("list_user"))


@staff_member_required
def deactivate_user(request, name):

    try:
        u = User.objects.get(username=name)
    except ObjectDoesNotExist:
        return redirect(reverse("list_user"))

    u.is_active = False
    u.save()
    return redirect(reverse("list_user"))


@staff_member_required
def activate_user(request, name):

    try:
        u = User.objects.get(username=name)
    except ObjectDoesNotExist:
        return redirect(reverse("list_user"))

    u.is_active = True
    u.save()
    return redirect(reverse("list_user"))

@staff_member_required
def make_admin(request, name):

    try:
        u = User.objects.get(username=name)
    except ObjectDoesNotExist:
        return redirect(reverse("list_user"))

    u.is_staff = True
    u.save()
    return redirect(reverse("list_user"))

@staff_member_required
def make_user(request, name):

    try:
        u = User.objects.get(username=name)
    except ObjectDoesNotExist:
        return redirect(reverse("list_user"))

    u.is_staff = False
    u.save()
    return redirect(reverse("list_user"))

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')

    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'accounts/password.html', {
        'form': form
    })
