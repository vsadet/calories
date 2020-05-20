from django.contrib import admin
from .models import Product, Dish


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'calories', 'protein', 'carbohydrates', 'fat')


admin.site.register(Product, ProductAdmin)


class DishAdmin(admin.ModelAdmin):
    list_display = ('dish_name', 'products_as_str')
    list_filter = ('products_names',)
    filter_horizontal = ('products_names',)


admin.site.register(Dish, DishAdmin)
