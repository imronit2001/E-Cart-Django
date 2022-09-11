from math import ceil
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from shop.models import Product


def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides': nSlides, 'range': range(
        1, nSlides), 'product': products}
    return render(request, 'shop/index.html', params)


def productView(request):
    return render(request, 'shop/product.html', {'products': Product.objects.all()})


def about(request):
    return HttpResponse("We are at about")


def contact(request):
    return HttpResponse("We are at contact")


def tracker(request):
    return HttpResponse("We are at tracker")


def search(request):
    return HttpResponse("We are at search")


def checkout(request):
    return HttpResponse("We are at checkout")
