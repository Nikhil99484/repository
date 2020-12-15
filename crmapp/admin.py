from django.contrib import admin

from  .models import Customers
from  .models import Products,Orders

class AdminCustomers(admin.ModelAdmin):
    list_display = ['name','email','mobile','created_date']
class AdminProducts(admin.ModelAdmin):
    list_display = ['name','price','category','description','created_date']
class AdminOrder(admin.ModelAdmin):
    list_display = ['customer','product','status','created_date']

admin.site.register(Customers,AdminCustomers)
admin.site.register(Products,AdminProducts)
admin.site.register(Orders,AdminOrder)

