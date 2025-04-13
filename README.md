# MyShop - Интернет-магазин на Django

## Описание проекта
MyShop - это полнофункциональное веб-приложение для электронной коммерции, разработанное с использованием Django. Проект позволяет пользователям просматривать товары, добавлять их в корзину и оформлять заказы с оплатой через Stripe.

## Основные функции
- Каталог товаров с категориями
- Корзина покупок
- Система оформления заказов
- Интеграция с платежной системой Stripe
- Асинхронная обработка задач с помощью Celery
- Отправка уведомлений по электронной почте

## Технологический стек
- **Backend**: Django
- **Платежная система**: Stripe
- **Асинхронные задачи**: Celery
- **Брокер сообщений**: RabbitMQ
- **База данных**: SQLite (разработка) / PostgreSQL (продакшен)
- **Frontend**: HTML, CSS, JavaScript

## Требования
- Python 3.8+
- Django 4.0+
- Stripe API ключи
- RabbitMQ или Redis (для Celery)

## Установка и настройка

### 1. Клонирование репозитория
```bash
git clone https://github.com/yourusername/myshop.git
cd myshop
```

### 2. Создание и активация виртуального окружения
```bash
python -m venv env
# Для Windows
env\Scripts\activate
# Для Unix/macOS
source env/bin/activate
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Настройка переменных окружения
Создайте файл `.env` в корневом каталоге проекта и добавьте следующие переменные:
```
SECRET_KEY=ваш_секретный_ключ_django
DEBUG=True
STRIPE_PUBLISHABLE_KEY=ваш_публичный_ключ_stripe
STRIPE_SECRET_KEY=ваш_секретный_ключ_stripe
STRIPE_WEBHOOK_SECRET=ваш_секретный_ключ_вебхука_stripe
```

### 5. Применение миграций
```bash
python manage.py migrate
```

### 6. Создание суперпользователя
```bash
python manage.py createsuperuser
```

### 7. Запуск сервера разработки
```bash
python manage.py runserver
```

### 8. Запуск Celery (в отдельном терминале)
#### Для Windows:
```bash
celery -A myshop worker -l info -P solo
```

#### Для Linux/macOS:
```bash
celery -A myshop worker -l info
```

## Использование Stripe Webhook
Для тестирования Stripe webhook локально можно использовать Stripe CLI:

1. Установите [Stripe CLI](https://stripe.com/docs/stripe-cli)
2. Авторизуйтесь:
   ```bash
   stripe login
   ```
3. Перенаправьте события на локальный сервер:
   ```bash
   stripe listen --forward-to http://localhost:8000/payment/webhook/
   ```

## Особенности проекта
- **Корзина покупок**: Реализована с использованием сессий Django
- **Платежная система**: Интеграция с Stripe Checkout для безопасной обработки платежей
- **Асинхронные задачи**: Отправка электронных писем и другие фоновые задачи обрабатываются с помощью Celery
- **Webhooks**: Обработка уведомлений от Stripe для подтверждения платежей
- **Оптимизация для Windows**: При запуске на Windows рекомендуется использовать параметр `-P solo` для Celery

## Структура проекта
```
myshop/
├── cart/                # Приложение корзины покупок
├── orders/              # Приложение заказов
├── payment/             # Приложение платежной системы
├── shop/                # Основное приложение магазина (каталог товаров)
├── myshop/              # Основной проект Django
│   ├── __init__.py      # Инициализация Celery
│   ├── settings.py      # Настройки проекта
│   ├── urls.py          # URL маршруты
│   └── celery.py        # Настройка Celery
└── media/               # Загружаемые файлы (изображения товаров и т.д.)
```

## Лицензия
[MIT License](LICENSE)
