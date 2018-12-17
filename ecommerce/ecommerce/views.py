from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

def mainPage(request):
    if request.method == 'GET':
        return render(request, 'ecommerce/home.html')
    elif request.method == 'POST':
        return HttpResponse('POST sent to main page')
