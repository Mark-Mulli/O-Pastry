from django.contrib import admin

from store.models import BasketItem


class BasketItemAdmin(admin.ModelAdmin):
    list_display = ["item_to_buy", "quantity", "order"]
    search_fields = ["item_to_buy", "quantity", "order"]


admin.site.register(BasketItem, BasketItemAdmin)
