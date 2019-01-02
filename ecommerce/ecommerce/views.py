from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from ProductManager.models import FeaturedProduct, Product

def mainPage(request):
    if request.method == 'GET':
        featured_products_id = FeaturedProduct.objects.values_list('product', flat=True)
        featured_products = Product.objects.filter(pk__in=featured_products_id).all()
        return render(request, 'ecommerce/home.html', {'featuredProducts': featured_products})
    elif request.method == 'POST':
        return HttpResponse('POST sent to main page')
