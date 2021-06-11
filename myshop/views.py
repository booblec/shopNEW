from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.contrib.auth.views import LoginView, LogoutView


def index (request):
    category = None
    categories = Category.objects.all()
    return render(
        request,
        'myshop/index.html',
        {
            'title':'Contact',
                      'category': category,
                      'categories': categories,
        }
    )




def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'myshop/product/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    category = None
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()
    return render(request, 'myshop/product/detail.html', {'product': product,
                                                          'cart_product_form': cart_product_form,
                                                          'categories': categories,
                                                          'products': products })

def contact(request):
    category = None
    categories = Category.objects.all()
    return render(
        request,
        'myshop/contact.html',
        {
            'title':'Contact',
                      'category': category,
                      'categories': categories,
        }
    )