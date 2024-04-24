from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Category)


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery
    extra = 1


class OptionInline(admin.TabularInline):
    fk_name = 'product'
    model = Option
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    inlines = [OptionInline, GalleryInline,]
    filter_horizontal = ("colors", )

admin.site.register(Color)