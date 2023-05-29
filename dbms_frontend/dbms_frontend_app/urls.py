from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert_product/', views.insert_product, name='insert_product'),
    path('update_product_price/', views.update_product_price, name='update_product_price'),
    path('update_payment_status/', views.update_payment_status, name='update_payment_status'),
    path('delete_store/', views.delete_store, name='delete_store'),
]
