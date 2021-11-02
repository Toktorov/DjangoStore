from django.contrib import admin
from apps.categories import models

# Register your models here.
class CategoryImageAdmin(admin.TabularInline):
    model = models.CategoryImage
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    inlines = [CategoryImageAdmin]

admin.site.register(models.Category, CategoryAdmin)
