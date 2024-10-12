from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Cart, Cart_item, Pormotion
from django.db import models

def index(request):
    products = Product.objects.all()
    latest_products = Product.objects.order_by('-id')[:3]
    promotions = Pormotion.objects.all()
    cart_item_count = count_cart_items(request)
    return render(request, 'alabeysi/index.html', {'products': products, 'latest_products': latest_products, 'cart_item_count': cart_item_count, 'promotions': promotions})

# Category views
def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    cart_item_count = count_cart_items(request)
    return render(request, 'alabeysi/category_products.html', {'category': category, 'products': products, 'cart_item_count': cart_item_count})


# Cart views
@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = Cart_item.objects.filter(cart=cart)
    cart_item_count = count_cart_items(request)
    total = sum(item.total_price for item in cart_items)
    return render(request, 'alabeysi/cart.html', {'cart_items': cart_items, 'total': total, 'cart_item_count': cart_item_count})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = Cart_item.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')
def count_cart_items(request):
    try: 
        cart = Cart.objects.get(user=request.user)
        return cart.cart_item_set.aggregate(total_items=models.Sum('quantity'))['total_items'] or 0
    except Cart.DoesNotExist:
        return 0
def Bag(request):
    products = Product.objects.filter(category__name='Bag')
    return render(request, 'alabeysi/Bag.html', {'products': products,})
   

def Hijab(request):
    products = Product.objects.filter(category__name='she')
    return render(request, 'alabeysi/Hijab.html', {'products': products,})
     

def Queen(request):
    products = Product.objects.filter(category__name='taako noocya')
    return render(request, 'alabeysi/Quen.html', {'products': products,})

def payment(request):
    cart = Cart.objects.get(user=request.user)
    total = cart.total_price
    return render(request, 'alabeysi/payment.html', {'total': total})

def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item = Cart_item.objects.get(cart=cart, product=product)
    cart_item.delete()
    return redirect('view_cart')

def promotion(request, promotion_id):
    promotion = get_object_or_404(Pormotion, id=promotion_id)
    return render(request, 'alabeysi/pormotion.html', {'promotion': promotion})


    
    