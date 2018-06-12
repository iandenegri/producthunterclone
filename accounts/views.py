from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method=='POST':
        # The user is submitting info to sign up
        if request.POST['password'] == request.POST['password-confirm']:
            try:
                user = User.objects.get(username =request.POST['username'])
                return render(request, 'accounts/signup.html',{'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password'])
                auth.login(request, user)
                return redirect('index')
        else:
            return render(request, 'accounts/signup.html',{'error':'Passwords must match and are case sensitive'})
    else:
        # The user is trying to sign up
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method=='POST':
        # The user submitted their info to login
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html',{'error':'Username or password is incorrect. Please verify your information and try again'})
    else:
        # The user wants to login
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('index')
