from django.contrib import admin

from seller.models import Item, Order


class ItemAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "description", "category", "image", "date_posted", "quantity"]
    search_fields = ["title", "price", "description", "category", "image", "date_posted", "quantity"]


admin.site.register(Item, ItemAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ["buyer", "buyer_anon", "order_date", "status"]
    search_fields = ["buyer", "buyer_anon", "order_date", "status"]


admin.site.register(Order, OrderAdmin)
