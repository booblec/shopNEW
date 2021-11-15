from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from myshop import forms
from django.contrib import admin
from .views import contact

app_name = 'myshop'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('edit/', views.edit, name='edit'),
    path('reset/', views.reset, name='reset'),
    path('account/', views.account, name='account'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('login/', LoginView.as_view (            
             template_name='myshop/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context= { 'title': 'Log in' }
         ),  name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('index/', views.index, name='index'),
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'
         ),
    path('<int:id>/<slug:slug>', views.product_detail,
         name='product_detail'),
    
]
