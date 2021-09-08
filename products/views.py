from django.shortcuts import render
from .models import Product


# Create your views here.
def all_products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }
    """ A view to show all products, including sorting and search queries """
    return render(request, 'products/products.html', context)
