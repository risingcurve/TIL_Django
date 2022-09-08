from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm # 로그인할 때
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import UserCreationForm # 회원가입할 때
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user()) # 유저의 정보
            return redirect('articles:index')
    else:
        form = AuthenticationForm()

    context = {
        'form' : form,
    }
    return render(request,'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # i, HALEY OH 로그인으로 넘어가길 원해요!
            user = form.save()
            auth_login(request, user)
            # index -> user가 회원가입하게
            # form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def delete(request):
    request.user.delete()
    return redirect('articles:index')

def update(request):

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        # 1. user의 정보가 먼저 보여줘야 하고
        # GET
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }

    return render(request, 'accounts/update.html', context)


    # 2. 수정 -> 요청
    # POST

    # if request

def change_password(request):
    if request.method == 'POST':
        # 비밀번호 변경된 거 저장
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)