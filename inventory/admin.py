from django.contrib import admin
from .models import VendorDetail,Item,StockDetail,Rack

# Register your models here.
admin.site.register(VendorDetail)
admin.site.register(Item)
admin.site.register(StockDetail)
admin.site.register(Rack)
