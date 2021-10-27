from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    Firstname = models.CharField(max_length = 100)
    Lastname = models.CharField(max_length = 100)
    House_number = models.CharField(max_length = 100)
    Barangay = models.CharField(max_length = 100)
    Municipality = models.CharField(max_length = 100)
    Province = models.CharField(max_length = 100)
    City = models.CharField(max_length = 100)
    Phone_Number = PhoneNumberField()
    Email = models.EmailField(max_length = 254)


    class meta:
        db_table ='clicktoeat_client'

 
class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    Order_Description = models.CharField(max_length = 20)
    Order_Type = models.CharField(max_length = 20)
    House_number = models.CharField(max_length = 20)
    Quantity = models.CharField(max_length = 50, null=True) 


    class meta:
        db_table ='clicktoeat_order'

class Rider(models.Model):
    id = models.BigAutoField(primary_key=True)
    Firstname = models.CharField(max_length = 20)
    Lastname = models.CharField(max_length = 20)
    Phone_Number = PhoneNumberField()
    Plate_Number  = models.CharField(max_length = 20)
    Make  = models.CharField(max_length = 20)

    class meta:
        db_table ='clicktoeat_rider'

class Store(models.Model):
    id = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length = 20)
    Address = models.CharField(max_length = 30)
    Telephone_Number = PhoneNumberField()

    class meta:
        db_table ='clicktoeat_store'

