# MyShop - Интернет-магазин на Django

**MyShop** — полнофункциональное e-commerce-приложение на Django.  
Пользователи могут просматривать каталог товаров, добавлять их в корзину и оплачивать заказ через Stripe.  
Проект поддерживает несколько языков благодаря **django-parler** и простое управление переводами через **django-rosetta**.

---

## Основные функции
- Каталог товаров с категориями
- Корзина, основанная на сессиях (работает и для неавторизованных)
- Рекомендации товаров на основе продаж (что покупают вместе)
- Оформление заказов + купоны на скидку  
- Интеграция с платежной системой Stripe (Оплата Stripe Checkout + проверка платежей через Webhook)
- Асинхронные задачи (e-mail, обработка платежа) на Celery + RabbitMQ/Redis
- Многоязычные названия, описания и SEO-slug’и (django-parler)
- Админ-панель с TranslatableAdmin (автоматическая генерация slug)  
- Управление переводами в админке через Rosetta  
- Docker-ready окружение (при желании можно использовать готовый `docker-compose.yml`)  

---

## Технологический стек
| Слой            | Технологии                                   |
|-----------------|----------------------------------------------|
| Backend         | Django, django-parler, django-rosetta        |
| База данных     | SQLite (dev) / PostgreSQL (prod)             |
| Асинхронность   | Celery + RabbitMQ / Redis                    |
| Платежи         | Stripe API                                   |
| Frontend        | HTML / CSS / JS (Bootstrap 5)                |

---

## Быстрый старт

### 1. Клонировать репозиторий
```bash
git clone https://github.com/Kiraogi/myshop.git
cd myshop
```

### 2. Создать и активировать виртуальное окружение
```bash
python -m venv env
# Windows
env\Scripts\activate
# Linux/macOS
source env/bin/activate
```

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```

### 4. Настройка переменных окружения  
Создайте `.env` рядом с `manage.py`:

```
# Django
SECRET_KEY=ваш_секретный_ключ
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
# Stripe
STRIPE_PUBLISHABLE_KEY=pk_test_***
STRIPE_SECRET_KEY=sk_test_***
STRIPE_WEBHOOK_SECRET=whsec_***
# E-mail (пример для gmail)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=example@gmail.com
EMAIL_HOST_PASSWORD=пароль
EMAIL_USE_TLS=True
```

### 5. Применить миграции и создать суперпользователя
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Собрать и скомпилировать сообщения перевода
```bash
# если добавили новые строки
python manage.py makemessages -l ru -l en
python manage.py compilemessages
```

### 7. Запуск
```bash
python manage.py runserver
```

### 8. Celery worker (во втором терминале)
```bash
# Linux/macOS
celery -A myshop worker -l info
# Windows
celery -A myshop worker -l info -P solo
```

---

## Webhook Stripe (локально)
```bash
# установить CLI
brew install stripe/stripe-cli/stripe
# авторизация
stripe login
# форвард событий
stripe listen --forward-to localhost:8000/payment/webhook/
```

---

## Работа с переводами
1. В админ-панели откройте _Rosetta_ (`/rosetta/`) и переведите строки интерфейса.  
2. Сохраните и нажмите **Compile** – строки станут доступны без перезапуска.  
3. Для моделей (Category, Product) просто добавьте перевод в соответствующей форме:  
   переключатель языка расположен вверху страницы объекта.

## Особенности проекта
- **Корзина покупок**: Реализована с использованием сессий Django
- **Платежная система**: Интеграция с Stripe Checkout для безопасной обработки платежей
- **Асинхронные задачи**: Отправка электронных писем и другие фоновые задачи обрабатываются с помощью Celery
- **Webhooks**: Обработка уведомлений от Stripe для подтверждения платежей
- **Оптимизация для Windows**: При запуске на Windows рекомендуется использовать параметр `-P solo` для Celery

---

## Структура проекта
```
myshop/
├─ cart/            # Приложение корзины покупок
├─ coupons/         # Приложение купонов
├─ orders/          # Приложение заказов
├─ payment/         # Приложение платежной системы (Stripe)
├─ shop/            # Основное приложение магазина (каталог товаров)
├─ myshop/          # Основной проект Django
│  ├─ __init__.py   # Инициализация Celery
│  ├─ celery.py     # конфигурация Celery
│  ├─ settings.py   # Настройки проекта
│  └─ urls.py       # URL маршруты включает i18n_patterns + Rosetta
└─ media/           # Загружаемые файлы (изображения товаров и т.д.)
```

---

## Полезные команды
| Команда | Назначение |
|---------|------------|
| `python manage.py makemessages -l <lang>` | собрать строки для нового языка |
| `python manage.py compilemessages` | скомпилировать .po в .mo |
| `python manage.py shell_plus` | интерактивная консоль (django-extensions) |
| `pytest -q` | запустить автотесты |

---