from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,Http404

from .models import Product
# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Hello world</h1>')
    context = {"name":"jisung"}
    return render(request, "home.html", context)

def product_detail_view(request,pk):
    # obj = Product.objects.get(pk=pk)
    try : 
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404
    return render(request, "products/detail.html", {"object": obj})

def product_list_view(request, *args, **kwargs):
    qs = Product.objects.all()
    context = {"object_list": qs}
    return render(request, "products/list.html", context)

def product_api_detail_view(request,pk, *args, **kwargs):
    obj = Product.objects.get(pk=pk)
    return JsonResponse({"id:": obj.id})
