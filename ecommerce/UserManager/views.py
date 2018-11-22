from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .components import SendActivationLink
from .models import ActivationCode
from .forms import UserSignupForm

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            SendActivationLink(user)
            return redirect('mainPage')
        else:
            return redirect('signup')
    elif request.method == 'GET':
        form = UserSignupForm()
        return render(request, 'UserManager/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

    return redirect('mainPage')

def activate(request, code):
    currentCode = ActivationCode.objects.get(code=code)
    if currentCode is not None:
        currentCode.delete()
        return HttpResponse('Your account was activated')
    else:
        return HttpResponse('Something went wrong')

def userProfile(request):
    return HttpResponse('Your profile')

def signout(request):
    logout(request)
    return redirect('mainPage')