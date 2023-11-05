from django.shortcuts import render, redirect
from .forms import UserRegisterationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def User_registeration(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user.first_name = cd['firstname']
            user.last_name = cd['lastname']
            user.save()
            messages.success(request, 'ثبت کاربر با موفقیت انجام پذیرفت', 'success')
            return redirect('home')

    else:
        form = UserRegisterationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'کاربر با موفقیت وارد شد', 'success')
                return redirect('home')
            else:
                messages.error(request, 'نام کاربری یا رمز اشتباه است', 'danger')
    form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request,'خروج موفق کاربر','success')
    return redirect('home')