from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,Http404

from .models import Product

from .form import ProductForm
# Create your views here.
def search_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Hello world</h1>')
    query = request.GET.get('q')
    qs = Product.objects.filter(title__icontains = query[0])
    print(qs)
    context = {"name":"jisung", "query": query}
    return render(request, "home.html", context)

def product_create_view(request, *args, **kwargs):
    # print(request.GET)
    # print(request.POST)
    if request.method == "POST":
        post_data = request.POST or None
        if post_data != None:
            my_form = ProductForm(request.POST)
            if my_form.is_valid():
                print(my_form.cleaned_data.get("title"))
                title_form_input = my_form.cleaned_data.get("title")
                Product.objects.create(title = title_form_input)
            # print(my_form.is_valid())
            # print("post_data", post_data)

    return render(request, "form.html", {})


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
