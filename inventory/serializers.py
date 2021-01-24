from rest_framework import serializers
from .models import VendorDetail, Item, Rack, StockDetail
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()



class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(max_length=255)
	password2 = serializers.CharField(max_length=255,required=False)

	class Meta:
		model = User
		fields=["username","password","password2","email"]
		extra_kwargs = {"password":{"write_only":True},"password2":{"write_only":True}}

		

	def validate(self,data):

		if data['password'] != data['password2']:
			raise ValidationError("Your password doesnot match!!")

		return data
'''
	def validate_email(self,value):
		if User.objects.filter(email__iexact = value).exists:
			raise ValidationError("User with this email already exists.")
		return value
'''


class VendorSerializer(serializers.ModelSerializer):
	user = UserSerializer()

	class Meta:
		model = VendorDetail
		fields=["id","user","name","company_name","contact","company_contact","pan_number"]


	

	
	# Function to Register User and Vendor

	def create(self, validated_data):
		user_data = validated_data.pop('user')
		user = User.objects.create(
			username = user_data['username'],
			password = user_data['password'],
			email=user_data['email'])
		user.is_staff = True
		user.save()
		vendor = VendorDetail.objects.create(user= user,**validated_data)
		vendor.save()
		return vendor

	def update(self,instance,validated_data):
		user_data = validated_data.pop('user')
		instance.name = validated_data.get('name')
		instance.company_name= validated_data.get('company_name')
		instance.contact = validated_data.get('contact')
		instance.company_contact = validated_data.get('company_contact')
		instance.pan_number = validated_data.get('pan_number')
		
		user_id = instance.user.id 
		if User.objects.get(id = user_id).exists():
			user = user_data.objects.get(id=user_id)
			user.name = user_data.get('name', user.name)
			user.company_name = user_data.get('company_name',user.company_name)
			user.contact = user_data.get('contact',user.contact)
			user.company_contact=user_data.get('company_contact',user.company_contact)
			user.pan_number=user_data.get('pan_number',user.pan_number)
			user.save()

		instance.save()



class ItemSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Item 
		fields =["id","item_name","item_code","local_name","item_category","item_limit","item_price"]



class RackSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rack
		fields=["rack_number"]


class StockDetailSerializer(serializers.ModelSerializer):
	
	item = ItemSerializer()
	rack = Rack()
	class Meta:
		model=StockDetail
		fields=["id","item","batch_number","value","bill_number","rack_number","bill_image","date","item_brand_name","remarks"]
		depth = 1


	def create(self,validated_data):
		user = self.context.get('request.user')
		vendor_detail = get_object_or_404(VendorDetail,user= user)
		item_id = validated_data.pop('item')
		item = get_object_or_404(Item,id=item_id)

		stock = StockDetail.create(user = user,item=item,vendor_detail= vendor_detail,**validated_data)
		stock.save()
		return stock




