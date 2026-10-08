from django.contrib import admin
from .models import KiranaItem, DailySale

@admin.register(KiranaItem)
class KiranaItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'category', 'quantity_in_stock', 'selling_price', 'cost_price')

@admin.register(DailySale)
class DailySaleAdmin(admin.ModelAdmin):
    list_display = ('item', 'qty_sold', 'sold_on')