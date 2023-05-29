from django.db import models

# Create your models here.

from django.db import models

class Customer(models.Model):
    C_ID = models.IntegerField(primary_key=True)
    C_Name = models.CharField(max_length=50)
    Contact_Num = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)

class CustomerReceipt(models.Model):
    C_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Payment_type = models.CharField(max_length=50)
    Payment_ID = models.IntegerField()
    Prod_id = models.IntegerField()
    Store_ID = models.IntegerField()
    Quantity = models.IntegerField()

class Employee(models.Model):
    E_ID = models.IntegerField(primary_key=True)
    E_Name = models.CharField(max_length=50)
    Contact_Num = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    Salary = models.CharField(max_length=50)

class PaymentPortal(models.Model):
    Payment_ID = models.IntegerField(primary_key=True)
    Payment_Type = models.CharField(max_length=50)
    Total_invoice = models.CharField(max_length=50)
    Payment_Status = models.CharField(max_length=50)

class Product(models.Model):
    Prod_ID = models.IntegerField(primary_key=True)
    Prod_Name = models.CharField(max_length=50)
    Prod_Desc = models.CharField(max_length=50)
    Prod_price = models.CharField(max_length=50)
    Prod_Stock = models.CharField(max_length=50)

class Store(models.Model):
    S_ID = models.IntegerField(primary_key=True)
    Manager_name = models.CharField(max_length=50)
    M_ID = models.IntegerField()
    Address = models.CharField(max_length=50)
    Num_Workers = models.IntegerField()

