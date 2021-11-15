from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.contrib.auth.views import LoginView, LogoutView


def index (request):

    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    products_last = Product.objects.order_by("-id")[0:4]
    category_man = Category.objects.order_by("slug")[0:5]
    category_woman = Category.objects.order_by("id")[0:5]
    category_dr = Category.objects.order_by("-id")[0:5]    
    return render(
        request,
        'myshop/index.html',
        {
            'title':'Contact',
                      'categories': categories,                   
                      'products': products,
                      'products_last': products_last,
                      'category_man': category_man,
                      'category_woman': category_woman,
                      'category_dr': category_dr,
        }
    )




def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    category_man = Category.objects.order_by("slug")[0:5]
    category_woman = Category.objects.order_by("id")[0:5]
    category_dr = Category.objects.order_by("-id")[0:5]
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'myshop/product/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products,
                       'category_man': category_man,
                      'category_woman': category_woman,
                      'category_dr': category_dr,
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    category = None
    categories = Category.objects.all()
    category_man = Category.objects.order_by("slug")[0:5]
    category_woman = Category.objects.order_by("id")[0:5]
    category_dr = Category.objects.order_by("-id")[0:5]
    cart_product_form = CartAddProductForm()
    return render(request, 'myshop/product/detail.html', {'product': product,
                                                          'cart_product_form': cart_product_form,
                                                          'categories': categories,
                                                           'category_man': category_man,
                      'category_woman': category_woman,
                      'category_dr': category_dr,
                                                         }
                                                          )

def contact(request):
    category = None
    categories = Category.objects.all()
    category_man = Category.objects.order_by("slug")[0:5]
    category_woman = Category.objects.order_by("id")[0:5]
    category_dr = Category.objects.order_by("-id")[0:5]
    return render(
        request,
        'myshop/contact.html',
        {
            'title':'Contact',
                      'category': category,
                      'categories': categories,
                       'category_man': category_man,
                      'category_woman': category_woman,
                      'category_dr': category_dr,
        }
    )

def about(request):
    category = None
    categories = Category.objects.all()
    category_man = Category.objects.order_by("slug")[0:5]
    category_woman = Category.objects.order_by("id")[0:5]
    category_dr = Category.objects.order_by("-id")[0:5]

    return render(
        request,
        'myshop/about.html',
        {
            'title':'О нас',
                      'category': category,
                      'categories': categories,
                      'category_man': category_man,
                      'category_woman': category_woman,
                      'category_dr': category_dr,
        }
    )


def register(request):
    category = None
    categories = Category.objects.all()
    category_man = Category.objects.order_by("slug")[0:5]
    category_woman = Category.objects.order_by("id")[0:5]
    category_dr = Category.objects.order_by("-id")[0:5]

    return render(
        request,
        'myshop/register.html',
        {
            'title':'Регистрация',
                      'category': category,
                      'categories': categories,
                      'category_man': category_man,
                      'category_woman': category_woman,
                      'category_dr': category_dr,
        }
    )

def reset(request):
    category = None
    categories = Category.objects.all()
    category_man = Category.objects.order_by("slug")[0:5]
    category_woman = Category.objects.order_by("id")[0:5]
    category_dr = Category.objects.order_by("-id")[0:5]

    return render(
        request,
        'myshop/reset.html',
        {
            'title':'Сброс',
                      'category': category,
                      'categories': categories,
                      'category_man': category_man,
                      'category_woman': category_woman,
                      'category_dr': category_dr,
        }
    )

def account(request):
    category = None
    categories = Category.objects.all()
    category_man = Category.objects.order_by("slug")[0:5]
    category_woman = Category.objects.order_by("id")[0:5]
    category_dr = Category.objects.order_by("-id")[0:5]

    return render(
        request,
        'myshop/account.html',
        {
            'title':'Аккаунт',
                      'category': category,
                      'categories': categories,
                      'category_man': category_man,
                      'category_woman': category_woman,
                      'category_dr': category_dr,
        }
    )

def edit(request):
    category = None
    categories = Category.objects.all()
    category_man = Category.objects.order_by("slug")[0:5]
    category_woman = Category.objects.order_by("id")[0:5]
    category_dr = Category.objects.order_by("-id")[0:5]

    return render(
        request,
        'myshop/editprofile.html',
        {
            'title':'Сброс',
                      'category': category,
                      'categories': categories,
                      'category_man': category_man,
                      'category_woman': category_woman,
                      'category_dr': category_dr,
        }
    )
