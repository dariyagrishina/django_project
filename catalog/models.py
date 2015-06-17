# -*- coding: utf-8 -*-
from django.forms import ModelForm
import django_filters
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.mail import send_mail, mail_managers


class Tag(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title


class Good(models.Model):
    name = models.CharField(max_length=200)
    name_lowercase = models.CharField(max_length=200)
    image = models.ImageField(upload_to='goods/')
    price = models.IntegerField()

    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.name

class GoodFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_type='contains', label="Наименование")
    price_lte = django_filters.NumberFilter(lookup_type='lte', label='До', name='price')
    price_gte = django_filters.NumberFilter(lookup_type='gte', label='От', name='price')

    class Meta:
        model = Good
        fields = ['name', 'price_gte', 'price_lte']


class Order(models.Model):
    phone_number = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    goods = models.ManyToManyField(Good)
    email = models.EmailField(max_length=25)

    ORDER_HANDLED = 'OH'
    ORDER_NOT_HANDLED = 'ONH'
    ORDER_HANDLED_CHOICES = (
        (ORDER_HANDLED, 'Заказ обработан'),
        (ORDER_NOT_HANDLED, 'Заказ не обработан'),
    )
    handle_order = models.CharField(max_length=3,
                                    choices=ORDER_HANDLED_CHOICES,
                                    default=ORDER_NOT_HANDLED)


    def __unicode__(self):
        return str(self.id)


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['phone_number', 'address', 'email']


@receiver(pre_save, sender=Order)
def send_email_by_handling(instance, **kwargs):
    if instance.id:
        old_order = Order.objects.get(pk=instance.id)
        if old_order.handle_order == 'ONH' and instance.handle_order == 'OH':
            message_to_customer = ' '.join(['Уважаемый клиент! Ваш заказ под номером', str(instance.id),
            'обработан и направлен по указанному Вами адресу.'])

            send_mail('Заказ обработан', message_to_customer,'dariya.grishina@gmail.com', [instance.email])


@receiver(post_save, sender=Order)
def send_email_about_order(instance, created, **kwargs):
    if created:
        message_to_customer = ' '.join(['Уважаемый клиент! Ваш заказ под номером', str(instance.id), 'поступил в обработку.'])
        message_to_manager = 'Поступил новый заказ.'

        send_mail('Подтверждение заказа', message_to_customer,
            'dariya.grishina@gmail.com', [instance.email])

        mail_managers(u'Заказ', message_to_manager)

