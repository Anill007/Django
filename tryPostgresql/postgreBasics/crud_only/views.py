from django.shortcuts import render
from .models import Product
from .forms import ProductUpload
import os
from django.conf import settings
from pathlib import Path

# Create your views here.


def product_list(request):
    if request.method == 'GET':
        data = Product.objects.all()
    return render(request, 'crud_only/base.html', {'product_list': data})


def upload(request):
    if request.method == 'GET':
        form = ProductUpload()
        return render(request, 'crud_only/upload.html', {'form': form})

    else:
        form = ProductUpload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        data = Product.objects.all()
        return render(request, 'crud_only/base.html', {'product_list': data})


def edit(request, id):
    if request.method == 'GET':
        data_unit = Product.objects.get(pk=id)
        data_form = ProductUpload(instance=data_unit)
        return render(request, 'crud_only/upload.html', {'form': data_form})

    else:
        product_instance = Product.objects.get(pk=id)
        to_del = Path(os.path.join(settings.MEDIA_ROOT,
                                   product_instance.Image.name))
        print(to_del)
        if os.path.exists(to_del):
            os.remove(to_del)

        to_del = Path(os.path.join(settings.MEDIA_ROOT,
                                   product_instance.ModelFile.name))
        if os.path.exists(to_del):
            os.remove(to_del)

        modify_instance = ProductUpload(
            request.POST, request.FILES, instance=product_instance)
        if modify_instance.is_valid():
            modify_instance.save()
        data = Product.objects.all()
        return render(request, 'crud_only/base.html', {'product_list': data})


def delete(request, id):
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        pi.delete()
        data = Product.objects.all()
        return render(request, 'crud_only/base.html', {'product_list': data})


def render_view(request):
    if request.method == 'POST':
        model_url = request.POST['url_value']
        print(model_url)
        index = model_url.rfind('/')
        index = index + 1
        fu = model_url[:index]
        lu = model_url[index:]
        print(fu)
        print(lu)
        fu = "http://127.0.0.1:8000" + fu
        return render(request, 'crud_only/dummybjs.html', {'fu': fu, 'lu': lu})
