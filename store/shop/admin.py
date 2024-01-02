from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )
class QuantityVariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'variant_name')
    search_fields = ('variant_name', )

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'category', 'quantity_available', 'quantity_type', 'image')
    list_filter = ('category', )
    search_fields = ('name', 'description')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(QuantityVariant, QuantityVariantAdmin)