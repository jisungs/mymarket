from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,Http404

from .models import Product
# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse('<h1>Hello world</h1>')

def product_detail_view(request,id):
    obj = Product.objects.get(id=id)
    try : 
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    return HttpResponse(f"<h1>Product title {obj.title}</h1>")

def product_api_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    return JsonResponse({"id:": obj.id})