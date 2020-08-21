from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Create your views here.

def prod_upload(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('prodlist')
    else:
        form = ProductForm()
    return render(request, 'uploadImageModelForm/upload.html', {'form': form})

def prod_list(request):
    prod = Product.objects.all()
    return render(request, 'uploadImageModelForm/list.html', {'prod': prod})

def prod_del(request, id):
    if request.method == 'POST':
        prod = Product.objects.get(pk = id)
        prod.delete()
        return redirect('prodlist')