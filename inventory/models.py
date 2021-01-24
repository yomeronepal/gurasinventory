from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

#Created models for VendorDetail
class VendorDetail(models.Model):
    
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    company_contact = models.CharField(max_length=255)
    pan_number = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name

#Created model Item
class Item(models.Model):
    
    item_name = models.CharField(max_length=255)
    item_code = models.CharField(max_length=255)
    local_name = models.CharField(max_length=255)
    item_category = models.CharField(max_length=255)
    item_limit = models.PositiveIntegerField(default = 1)
    item_price	= models.FloatField()
    

    def __str__(self):
        return self.item_name

#Created models Rack
class Rack(models.Model):
    rack_number = models.PositiveIntegerField()

    def __int__(self):
        return self.rack_number

class StockDetail(models.Model):
    item = models.ForeignKey(Item,on_delete=models.DO_NOTHING)
    vendor_detail = models.ForeignKey(VendorDetail,on_delete=models.DO_NOTHING)
    batch_number = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    value = models.FloatField()
    bill_number = models.CharField(max_length=255)
    rack_number = models.ForeignKey(Rack,on_delete=models.DO_NOTHING,null=True)
    bill_image = models.ImageField(upload_to="bill/",null=True)
    date = models.DateField(auto_now_add=True)
    item_brand_name = models.CharField(max_length=255)
    remarks = models.TextField()

    def __str__(self):
        return self.item.item_name











'''
# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    item_name = models.CharField(max_length=255)
    item_code = models.CharField(max_length=255)
    local_name = models.CharField(max_length=255)
    item_category = models.CharField(max_length=255)
    item_limit = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return self.item_name

class VendorDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    company_contact = models.CharField(max_length=255)
    pan_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Rack(models.Model):
    rack_number = models.PositiveIntegerField()

    def __str__(self):
        return self.rack_number
class StockDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    item = models.ForeignKey(Item,on_delete=models.DO_NOTHING)
    vendor_detail = models.ForeignKey(VendorDetail,on_delete=models.DO_NOTHING)
    batch_number = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    value = models.FloatField()
    bill_number = models.CharField(max_length=255)
    rack_number = models.ForeignKey(Rack,on_delete=models.DO_NOTHING,null=True)
    bill_image = models.ImageField(upload_to="bill/")
    date = models.DateField(auto_now_add=True)
    item_brand_name = models.CharField(max_length=255)
    remarks = models.TextField()

    def __str__(self):
        return self.item.item_name


class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    company_contact = models.CharField(max_length=255)
    pan_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class LostDamage(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    item = models.ForeignKey(Item,on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    batch_number = models.CharField(max_length=255)

    def __str__(self):
        return self.item.item_name


class StockOut(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    item = models.ForeignKey(Item,on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    bill_number = models.CharField(null=True,blank=True,max_length=100)

'''

