from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import VendorSerializer,ItemSerializer, StockDetailSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from braces.views import CsrfExemptMixin
from .models import Item, VendorDetail, StockDetail
from django.shortcuts import get_object_or_404

# Create your views here.

class VendorRegistration(APIView):

	def post(self, request):
		serializer = VendorSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"msg":"Account Sucessfully Created"}, status= status.HTTP_200_OK)
		return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class AddItemAPI(APIView):
	permissions_classes = [IsAuthenticated,]


	def get(self,request):
		query_set = Item.objects.all()
		serializer = ItemSerializer(query_set,many = True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request):
		serializer = ItemSerializer(data= request.data)
		if serializer.is_valid():
			serializer.save(user =request.user)
			return Response(serializer.data, status = status.HTTP_200_OK)
		return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class ItemDetailAPI(APIView):
	permissions_classes = [IsAuthenticated,]

	def get(self,request,id):
		query_set = get_object_or_404(Item, id= id)
		serializer = ItemSerializer(query_set)
		return Response(serializer.data,status=status.HTTP_200_OK)

	def put(self,request,id):
		query_set = get_object_or_404(Item, id=id)
		serializer = ItemSerializer(query_set,data= request.data, partial= True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data , status= status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,id):
		query_set = get_object_or_404(Item,id = id)
		query_set.delete()
		msg={"msg":"Item deleted sucessfully"}
		return Response(msg,status= status.HTTP_200_OK)


class StockDetailAPIView(APIView):
	permissions_classes =[IsAuthenticated,]

	def post (self,request):
		serializer = StockDetailSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status = status.HTTP_200_OK)
		return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

	def get(self,request):
		qs = StockDetail.objects.all()
		serializer = StockDetailSerializer(qs, many=True)
		return Response(serializer.data , status=status.HTTP_200_OK)

	
