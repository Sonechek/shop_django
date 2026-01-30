# shop_django

Проектик

## 📌 Требования

* Docker Desktop (Windows) или Docker Engine
* Docker Compose
* Python 3.10+

**Проверка установок:**

```powershell
docker --version
docker compose version
python --version
```

## 🚀 Пошаговый запуск проекта

1. **Поднять контейнер с PostgreSQL**

```powershell
docker compose up -d
```

2. **Установить зависимости**

```powershell
pip install -r requirements.txt
```

3. **Применить миграции**

```powershell
python manage.py migrate
```

4. **Запустить команду setup для наполнения базы**

```powershell
python manage.py setup
```

> Команда создаёт тестовые данные.

5. **Запустить сервер Django**

```powershell
python manage.py runserver
```
