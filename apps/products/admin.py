from django.contrib import admin
from apps.products import models


# Register your models here.
class ProductImageAdmin(admin.TabularInline):
    model = models.ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    inlines = [ProductImageAdmin]

admin.site.register(models.Product, ProductAdmin)
