# -*- coding: utf-8 -*-
from __future__ import absolute_import

from celery import shared_task
from django.core.mail import send_mail, mail_managers


@shared_task
def send_mail_about_order(number, email):
    message_to_customer = ' '.join(['Уважаемый клиент! Ваш заказ под номером', str(number), 'поступил в обработку.'])
    message_to_manager = 'Поступил новый заказ.'

    send_mail('Подтверждение заказа', message_to_customer,
        'dariya.grishina@gmail.com', [email], fail_silently=False)

    mail_managers(u'Заказ', message_to_manager, fail_silently=False)
    return

@shared_task
def send_mail_handled(number, email):
    message_to_customer = ' '.join(['Уважаемый клиент! Ваш заказ под номером', str(number),
        'обработан и направлен по указанному Вами адресу.'])

    send_mail('Заказ обработан', message_to_customer,'dariya.grishina@gmail.com', [email],
        fail_silently=False)
    return
