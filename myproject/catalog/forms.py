from django import forms
from .models import Category, Product, Warehouse, Stock


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "description", "price", "product_type", "sku"]


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ["name"]


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["product", "warehouse", "quantity"]
