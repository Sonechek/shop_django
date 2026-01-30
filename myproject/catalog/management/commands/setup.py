from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from catalog.models import User, Category, Product, Warehouse, Stock

class Command(BaseCommand):
    help = "Заполняет базу данными и создаёт роли с правами"

    def handle(self, *args, **kwargs):
        # ---------- Очистка базы ----------
        Stock.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.all().delete()
        Warehouse.objects.all().delete()
        User.objects.exclude(is_superuser=True).delete()  # сохраняем суперпользователя

        self.stdout.write("База очищена!")

        # ---------- Пользователи ----------
        users_data = [
            {'username': 'admin', 'role': 'admin', 'password': 'admin123'},
            {'username': 'manager1', 'role': 'manager', 'password': 'manager123'},
            {'username': 'employee1', 'role': 'employee', 'password': 'employee123'},
            {'username': 'employee2', 'role': 'employee', 'password': 'employee123'},
        ]

        for u in users_data:
            user = User(username=u['username'], role=u['role'])
            user.set_password(u['password'])
            user.save()
            self.stdout.write(f"Создан пользователь: {user.username}")

        # ---------- Категории ----------
        categories_data = [
            {'name': 'Электроника', 'description': 'Телефоны, ноутбуки, аксессуары'},
            {'name': 'Одежда', 'description': 'Мужская и женская одежда'},
            {'name': 'Продукты питания', 'description': 'Сухие и свежие продукты'},
            {'name': 'Бытовая химия', 'description': 'Чистящие средства, моющие'},
        ]
        for c in categories_data:
            Category.objects.create(name=c['name'], description=c['description'])
        self.stdout.write("Категории созданы!")

        # ---------- Продукты ----------
        products_data = [
            {'name': 'iPhone 15', 'category': 'Электроника', 'description': 'Смартфон Apple', 'price': 120000.00, 'product_type': 'product', 'sku': 'IP15-001'},
            {'name': 'Ноутбук ASUS', 'category': 'Электроника', 'description': 'Мощный игровой ноутбук', 'price': 80000.00, 'product_type': 'product', 'sku': 'ASUS-GL-01'},
            {'name': 'Футболка мужская', 'category': 'Одежда', 'description': 'Хлопковая футболка', 'price': 1200.00, 'product_type': 'product', 'sku': 'TSHIRT-M-01'},
            {'name': 'Молоко 1л', 'category': 'Продукты питания', 'description': 'Свежие молочные продукты', 'price': 120.00, 'product_type': 'product', 'sku': 'MILK-001'},
            {'name': 'Уборка дома', 'category': 'Бытовая химия', 'description': 'Сервис уборки дома', 'price': 5000.00, 'product_type': 'service', 'sku': 'CLEAN-001'},
        ]
        for p in products_data:
            category = Category.objects.get(name=p['category'])
            Product.objects.create(
                name=p['name'],
                category=category,
                description=p['description'],
                price=p['price'],
                product_type=p['product_type'],
                sku=p['sku']
            )
        self.stdout.write("Продукты созданы!")

        # ---------- Склады ----------
        warehouses_data = ['Центральный склад', 'Склад №1', 'Склад №2']
        for w_name in warehouses_data:
            Warehouse.objects.create(name=w_name)
        self.stdout.write("Склады созданы!")

        # ---------- Остатки ----------
        stock_data = [
            {'product_sku': 'IP15-001', 'warehouse': 'Центральный склад', 'quantity': 50},
            {'product_sku': 'ASUS-GL-01', 'warehouse': 'Центральный склад', 'quantity': 20},
            {'product_sku': 'TSHIRT-M-01', 'warehouse': 'Склад №1', 'quantity': 100},
            {'product_sku': 'MILK-001', 'warehouse': 'Склад №2', 'quantity': 200},
            {'product_sku': 'CLEAN-001', 'warehouse': 'Центральный склад', 'quantity': 10},
        ]
        for s in stock_data:
            product = Product.objects.get(sku=s['product_sku'])
            warehouse = Warehouse.objects.get(name=s['warehouse'])
            Stock.objects.create(product=product, warehouse=warehouse, quantity=s['quantity'])
        self.stdout.write("Остатки на складах созданы!")

        # ---------- Роли и права ----------
        manager_group, _ = Group.objects.get_or_create(name="Manager")
        warehouse_group, _ = Group.objects.get_or_create(name="WarehouseWorker")

        manager_permissions = Permission.objects.filter(
            content_type__app_label="catalog",
            content_type__model__in=["product", "category"]
        )
        manager_group.permissions.set(manager_permissions)

        warehouse_permissions = Permission.objects.filter(
            content_type__app_label="catalog",
            content_type__model="stock"
        )
        warehouse_group.permissions.set(warehouse_permissions)

        self.stdout.write(self.style.SUCCESS("Роли и права успешно созданы!"))
        self.stdout.write(self.style.SUCCESS("База данных полностью заполнена!"))
