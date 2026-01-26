from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Category, Product, Warehouse, Stock
from .forms import CategoryForm, ProductForm, WarehouseForm, StockForm
from .decorators import role_required


@login_required
def home(request):
    if request.user.is_authenticated:
        return render(request, "catalog/home.html")  # главная страница
    return redirect("login")

# Категории

@login_required
@role_required(["admin", "manager"])
def category_list(request):
    categories = Category.objects.all()
    return render(request, "catalog/category_list.html", {"categories": categories, "title": "Категории"})


@login_required
@role_required(["admin", "manager"])
def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("category_list")
    return render(request, "catalog/form.html", {
        "form": form,
        "title": "Категория",
        "list_url": reverse("category_list")
    })


@login_required
@role_required(["admin", "manager"])
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect("category_list")
    return render(request, "catalog/form.html", {
        "form": form,
        "title": "Категория",
        "list_url": reverse("category_list")
    })


@login_required
@role_required(["admin"])
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect("category_list")
    return render(request, "catalog/confirm_delete.html", {
        "object": category,
        "title": "Категория",
        "list_url": reverse("category_list")
    })


# Товары

@login_required
@role_required(["admin", "manager"])
def product_list(request):
    products = Product.objects.select_related("category").all()
    return render(request, "catalog/product_list.html", {"products": products, "title": "Товары"})


@login_required
@role_required(["admin", "manager"])
def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("product_list")
    return render(request, "catalog/form.html", {
        "form": form,
        "title": "Товар",
        "list_url": reverse("product_list")
    })


@login_required
@role_required(["admin", "manager"])
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect("product_list")
    return render(request, "catalog/form.html", {
        "form": form,
        "title": "Товар",
        "list_url": reverse("product_list")
    })


@login_required
@role_required(["admin"])
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("product_list")
    return render(request, "catalog/confirm_delete.html", {
        "object": product,
        "title": "Товар",
        "list_url": reverse("product_list")
    })


@login_required
@role_required(["admin", "manager"])
def product_print(request, pk):
    product = get_object_or_404(Product, pk=pk)
    stocks = Stock.objects.filter(product=product)
    return render(request, "catalog/product_print.html", {
        "product": product,
        "stocks": stocks
    })


# Склады

@login_required
@role_required(["admin", "employee"])
def warehouse_list(request):
    warehouses = Warehouse.objects.all()
    return render(request, "catalog/warehouse_list.html", {"warehouses": warehouses, "title": "Склады"})


@login_required
@role_required(["admin", "employee"])
def warehouse_create(request):
    form = WarehouseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("warehouse_list")
    return render(request, "catalog/form.html", {
        "form": form,
        "title": "Склад",
        "list_url": reverse("warehouse_list")
    })


@login_required
@role_required(["admin", "employee"])
def warehouse_update(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)
    form = WarehouseForm(request.POST or None, instance=warehouse)
    if form.is_valid():
        form.save()
        return redirect("warehouse_list")
    return render(request, "catalog/form.html", {
        "form": form,
        "title": "Склад",
        "list_url": reverse("warehouse_list")
    })


@login_required
@role_required(["admin", "employee"])
def warehouse_delete(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)
    if request.method == "POST":
        warehouse.delete()
        return redirect("warehouse_list")
    return render(request, "catalog/confirm_delete.html", {
        "object": warehouse,
        "title": "Склад",
        "list_url": reverse("warehouse_list")
    })


# Остатки на складах

@login_required
@role_required(["admin", "employee"])
def stock_list(request):
    stock_items = Stock.objects.select_related("product", "warehouse").all()
    return render(request, "catalog/stock_list.html", {"stock_items": stock_items, "title": "Остатки на складах"})


@login_required
@role_required(["admin", "employee"])
def stock_create(request):
    form = StockForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("stock_list")
    return render(request, "catalog/form.html", {
        "form": form,
        "title": "Запись на складе",
        "list_url": reverse("stock_list")
    })


@login_required
@role_required(["admin", "employee"])
def stock_update(request, pk):
    stock_item = get_object_or_404(Stock, pk=pk)
    form = StockForm(request.POST or None, instance=stock_item)
    if form.is_valid():
        form.save()
        return redirect("stock_list")
    return render(request, "catalog/form.html", {
        "form": form,
        "title": "Запись на складе",
        "list_url": reverse("stock_list")
    })


@login_required
@role_required(["admin", "employee"])
def stock_delete(request, pk):
    stock_item = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        stock_item.delete()
        return redirect("stock_list")
    return render(request, "catalog/confirm_delete.html", {
        "object": stock_item,
        "title": "Запись на складе",
        "list_url": reverse("stock_list")
    })
