from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlace
from .forms import CustomerRegistrationForm
from django.contrib import messages

# Create your views here.

# def home(request):
#     return render(request, 'app/home.html')


class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        accessories = Product.objects.filter(category='AC')
        electronics = Product.objects.filter(category='EL')
        homedecors = Product.objects.filter(category='HD')
        footwears = Product.objects.filter(category='FT')
        bags = Product.objects.filter(category='BG')
        beautyproducts = Product.objects.filter(category='BT')
        return render(request, 'app/home.html', {'mobiles': mobiles, 'laptops': laptops, 'topwears': topwears, 'bottomwears': bottomwears, 'accessories': accessories, 'electronics': electronics, 'homedecors': homedecors, 'footwears': footwears, 'bags': bags, 'beautyproducts': beautyproducts})


# def product_detail(request):
#     return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product': product})


def add_to_cart(request):
    return render(request, 'app/addtocart.html')


def buy_now(request):
    return render(request, 'app/buynow.html')


def profile(request):
    return render(request, 'app/profile.html')


def address(request):
    return render(request, 'app/address.html')


def orders(request):
    return render(request, 'app/orders.html')


def change_password(request):
    return render(request, 'app/changepassword.html')


# def mobile(request, data=None):
#     if data == None:
#         mobiles = Product.objects.filter(category='M')
#     elif data == 'Redmi' or data == "Samsung":
#         mobiles = Product.objects.filter(category='M').filter(brand=data)
#     return render(request, 'app/mobile.html', {'mobiles': mobiles})

def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data in ['Redmi', 'Samsung', 'Apple', 'Vivo', 'Oppo', 'Realme', 'Motorola', 'Google']:
        mobiles = Product.objects.filter(category='M', brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(
            category='M').filter(discounted_price__lt=10000)
    elif data == 'above':
        mobiles = Product.objects.filter(
            category='M').filter(discounted_price__gt=10000)
    return render(request, 'app/mobile.html', {'mobiles': mobiles})


def login(request):
    return render(request, 'app/login.html')


# def customerregistration(request):
#     return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(
                request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'app/customerregistration.html', {'form': form})


def checkout(request):
    return render(request, 'app/checkout.html')
