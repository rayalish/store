from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'category', 'quantity_available', 'image')
    list_filter = ('category', )
    search_fields = ('name', 'description')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)