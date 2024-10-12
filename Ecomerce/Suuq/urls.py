from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),    
    
    path('view_cart/', views.view_cart , name='view_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('Bag/', views.Bag, name='Bag'),
    path('Hijab/', views.Hijab, name='she'),
    path('Queen/', views.Queen, name='taako noocya'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('payment/', views.payment, name='payment'),
    path('pormotion/<int:promotion_id>/', views.promotion, name='promotion'),
    
   
    



    ]
