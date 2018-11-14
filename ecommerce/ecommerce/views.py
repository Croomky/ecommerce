from django.shortcuts import render
from django.http import JsonResponse

def mainPage(request):
    if request.method == 'GET':
        return render(request, 'ecommerce/home.html')