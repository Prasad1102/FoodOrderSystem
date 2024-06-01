from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.

def home(request):
  return render(request, "home.html")

def home_2(request):
  return render(request, "home.html")

def aboutPage(request):
  return render(request, "about.html")

def userPage(request):
  return render(request, "user.html")

def menuePage(request):
  products = Product.objects.all()
  return render(request, "menue.html", {'products':products})

def reservationPage(request):
  return render(request, "reservation.html")

@login_required(login_url="/login_page")
def addMenue(request):
  if request.method == "POST":
    data = request.POST
    product_name = data.get('product_name')
    product_image = request.FILES.get('product_image')
    product_slug = data.get('product_slug')
    product_description = data.get('product_description')
    product_price = data.get('product_price')
    product_demo_price = data.get('product_demo_price')
    quantity = data.get('quantity')

    Product.objects.create(
      product_name = product_name,
      product_slug = product_slug,
      product_image = product_image,
      product_description = product_description,
      product_price = product_price,
      product_demo_price = product_demo_price,
      quantity = quantity
    )
    return redirect("/addMenue")
  return render(request, "addMenue.html")


def register_page(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    password = request.POST.get('password')

    user = User.objects.filter(username=username)

    if user.exists():
      messages.info(request, "Username already exists.")
      return redirect('/register')

    user = User.objects.create(
      username=username,
      first_name=first_name,
      last_name=last_name,
    )
    user.set_password(password)
    user.save()
    messages.info(request, "Account Created Succesfully")

    return redirect('/register')
  return render(request, "register.html")


def login_page(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    if not User.objects.filter(username=username).exists():
      messages.info(request, "Invalid UserName")
      return redirect('/login_page')

    user = authenticate(username = username, password = password)
    if user is None:
      messages.info(request, "Invalid Password")
      return redirect('/login_page')
    else:
      login(request, user)
      return redirect('/menue')
    
  return render(request, "login.html")

def logout_page(request):
  logout(request)
  return redirect('/login_page')


  # _____________________(ADD TO CART)________________________________________________________
class ProductWrapper:
    def __init__(self, product):
        self.id = str(product.id)  # Convert UUID to string
        self.name = product.product_name
        self.price = product.product_price
        self.image = product.product_image
    def __getattr__(self, item):
        return getattr(self.__dict__, item)

@login_required(login_url="/login_page")
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    wrapped_product = ProductWrapper(product)  # Use the wrapper
    cart.add(product=wrapped_product)
    return redirect("/menue")

@login_required(login_url="/login_page")
def item_clear(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    wrapped_product = ProductWrapper(product)  # Use the wrapper
    cart.remove(product=wrapped_product)
    return redirect("/cart-detail")

@login_required(login_url="/login_page")
def item_increment(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    wrapped_product = ProductWrapper(product)  # Use the wrapper
    cart.add(product=wrapped_product)
    return redirect("/cart-detail")

@login_required(login_url="/login_page")
def item_decrement(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    wrapped_product = ProductWrapper(product)  # Use the wrapper
    cart.decrement(product=wrapped_product)
    return redirect("/cart-detail")

@login_required(login_url="/login_page")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("/")

@login_required(login_url="/login_page")
def cart_detail(request):
  cart = Cart(request)
  cart_items = []
  total_price  = 0
  for item in cart.cart.values():
    price = float(item['price'])
    quantity = item['quantity']
    total_price += price * quantity

    cart_items.append({
      'id': item['product_id'],
      'name': item['name'],
      'price': item['price'],
      'quantity': item['quantity'],
      'image': item['image']
    })

  context = {
    'cart_items': cart_items,
    'total_price': total_price
  }
  return render(request, 'cartDetail.html', context)