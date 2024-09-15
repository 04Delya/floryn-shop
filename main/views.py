from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product

# Create your views here.
def show_main(request):
    products = Product.objects.all()

    context = {
        'npm' : '2306245586',
        'name': 'Delya Ardiyanti',
        'class': 'PBP A',
        'products': products
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)
