from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .forms import SigninForm

def mainPage(request):
    if request.method == 'GET':
        loginForm = SigninForm()
        return render(request, 'ecommerce/home.html', { 'loginForm': loginForm })
    elif request.method == 'POST':
        return HttpResponse('POST sent to main page')
