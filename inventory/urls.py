from django.urls import path
from .views import VendorRegistration, AddItemAPI,FacebookLogin, ItemDetailAPI, StockDetailAPIView
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('',VendorRegistration.as_view(),name="vendor-registration" ),
    path('item/',csrf_exempt(AddItemAPI.as_view()),name= "add-item"),
    path('item-detail/<int:id>',ItemDetailAPI.as_view(),name="item-detail"),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    path('stock-detail/',StockDetailAPIView.as_view(),name ='stock-detail')
    
]