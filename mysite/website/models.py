from django.db import models
from django.utils.html import format_html


class Product(models.Model):
    product_name = models.CharField(max_length=200, verbose_name='Название')
    calories = models.IntegerField(verbose_name='Калории')
    protein = models.IntegerField(verbose_name='Белки')
    carbohydrates = models.IntegerField(verbose_name='Углеводы')
    fat = models.IntegerField(verbose_name='Жиры')

    def __str__(self):
        return self.product_name


class Dish(models.Model):
    dish_name = models.CharField(max_length=200, verbose_name='Название блюда')
    products_names = models.ManyToManyField(Product, verbose_name='Продукты')

    def products_as_str(self):
        result = ''
        for product in self.products_names.all():  # Вот тут мы берем все инградиенты b обходим их
            result += f'<strong>{product.product_name}</strong> ({product.calories} kKal)<br>\n'
        return format_html(result)

    products_as_str.short_description = 'Продукты'