from django.contrib import admin

from .models import (
    Supplier,
    Buyer,
    Season,
    Drop,
    Product,
    Order,
    Delivery
)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']


class BuyerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Season)
admin.site.register(Drop)
admin.site.register(Product)
# admin.site.register(Order)        # <-- REMOVE this line – it's duplicated
admin.site.register(Delivery)


# Keep only this registration for Order (decorator style)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'supplier', 'product', 'buyer', 'status', 'created_date']
    list_editable = ['status']
    list_filter = ['status']
admin.site.register(Order)
admin.site.register(Delivery)

