from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from io import BytesIO
from celery import shared_task
import weasyprint

from orders.models import Order

@shared_task
def payment_completed(order_id):
    """
    Задание по отправке уведомлений по электронной почте
    при успешной оплате заказа.
    """
    order = Order.objects.get(id=order_id)
    # Создать invoice e-mail
    subject = f'My Shop - Invoice no. {order.id}'
    message = 'Please, find attached the invoice for your recent purchase.'
    email = EmailMessage(subject, message, 'admin@myshop.com', [order.email])
    # Сгенерировать PDF
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT / 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    # Прикрепить PDF-файл
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')
    # Отправить электронное письмо
    email.send()
