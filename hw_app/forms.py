# Homework 4
# Задание №6
# Доработаем задачу про клиентов, заказы и товары из прошлого семинара.
# Создайте форму для редактирования товаров в базе данных.

# Домашнее задание
# Измените модель продукта, добавьте поле для хранения фотографии продукта.
# Создайте форму, которая позволит сохранять фото.


from django import forms
from .models import Product

class ProductEditForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    name = forms.CharField(max_length=100)
    description = forms.CharField()
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity = forms.IntegerField()


class ImageForm(forms.Form):
    image = forms.ImageField()
