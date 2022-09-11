from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from shop.models import Product


def index(request):
    return render(request, 'shop/index.html')


def productView(request):
    return render(request, 'product.html', {'products': Product.objects.all()})


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
