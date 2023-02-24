from django.db import models


class Product(models.Model):
    calories = models.IntegerField(max_length=4)
    protein = models.IntegerField(max_length=4)
    carbohydrates = models.IntegerField(max_length=4)
    fat = models.IntegerField(max_length=4)


class Consumed(models.Model):
    grams = models.IntegerField(max_length=3)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, blank=True)
