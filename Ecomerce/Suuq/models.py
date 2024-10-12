from django.db import models
from django.contrib.auth.models import User 
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render 
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Pormotion(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
    @property
    def total_price(self):
        return self.product.price * self.quantity
    
class Cart_item(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
   

    def __str__(self):
        return f"{self.cart.user.username} - {self.product.name}"
    @property
    def total_price(self):
        return self.product.price * self.quantity
    def payment(request):
        cart = Cart.objects.get(user=request.user)
        total = cart.total_price
        return render(request, 'alabeysi/payment.html', {'total': total})
    
    def remove_from_cart(request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item = Cart_item.objects.get(cart=cart, product=product)
        cart_item.delete()
        return redirect('cart')
      
    

