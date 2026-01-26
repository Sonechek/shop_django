from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="catalog/login.html"
        ),
        name="login"
    ),

    path("logout/", auth_views.LogoutView.as_view(), name="logout"),



    # Категория
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/update/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),

    # Товары
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/update/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('products/<int:pk>/print/', views.product_print, name='product_print'),

    # Склады
    path('warehouses/', views.warehouse_list, name='warehouse_list'),
    path('warehouses/create/', views.warehouse_create, name='warehouse_create'),
    path('warehouses/<int:pk>/update/', views.warehouse_update, name='warehouse_update'),
    path('warehouses/<int:pk>/delete/', views.warehouse_delete, name='warehouse_delete'),

    # Остатки на складах
    path('stock/', views.stock_list, name='stock_list'),
    path('stock/create/', views.stock_create, name='stock_create'),
    path('stock/<int:pk>/update/', views.stock_update, name='stock_update'),
    path('stock/<int:pk>/delete/', views.stock_delete, name='stock_delete'),

    
]
