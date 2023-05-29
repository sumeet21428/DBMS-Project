from django.shortcuts import render
from django.db.models import F

# Create your views here.
from django.shortcuts import render
from .models import Product, PaymentPortal, Store

def index(request):
    return render(request, 'index.html')

def insert_product(request):
    if request.method == 'POST':
        prod_id = request.POST['prod_id']
        prod_name = request.POST['prod_name']
        prod_type = request.POST['prod_type']
        prod_price = request.POST['prod_price']
        prod_stock = request.POST['prod_stock']
        
        product = Product(Prod_ID=prod_id, Prod_Name=prod_name, Prod_Desc=prod_type,
                          Prod_price=prod_price, Prod_Stock=prod_stock)
        product.save()
        
        return render(request, 'success.html')
    else:
        return render(request, 'insert_product.html')

def update_product_price(request):
    if request.method == 'POST':
        Product.objects.filter(Prod_Stock__gt=0).update(Prod_price=F('Prod_price') * 0.5)
        
        return render(request, 'success.html')
    else:
        return render(request, 'update_product_price.html')

def update_payment_status(request):
    if request.method == 'POST':
        payment_type = request.POST['payment_type']
        
        PaymentPortal.objects.filter(Payment_Type=payment_type).update(Payment_Status='PAID')
        
        return render(request, 'success.html')
    else:
        return render(request, 'update_payment_status.html')

def delete_store(request):
    if request.method == 'POST':
        num_workers = request.POST['num_workers']
        
        Store.objects.filter(Num_Workers__lt=num_workers).delete()
        
        return render(request, 'success.html')
    else:
        return render(request, 'delete_store.html')
