from django.db import models


class product(models.Model):
    product_name = models.CharField(max_length=200, verbose_name='Название')
    calories = models.IntegerField(verbose_name='Калории')
    protein = models.IntegerField(verbose_name='Белки')
    carbohydrates = models.IntegerField(verbose_name='Углеводы')
    fat = models.IntegerField(verbose_name='Жиры')

    def __str__(self):
        return self.product_name


class dish(models.Model):
    dish_name = models.CharField(max_length=200, verbose_name='Название блюда')
    products_names = models.CharField(max_length=2000, verbose_name='Название продуктов')
    calories = models.IntegerField(verbose_name='Калории')
    protein = models.IntegerField(verbose_name='Белки')
    carbohydrates = models.IntegerField(verbose_name='Углеводы')
    fat = models.IntegerField(verbose_name='Жиры')

    def __str__(self):
        return self.dish_name
