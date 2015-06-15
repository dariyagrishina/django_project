# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.views.generic.detail import DetailView, BaseDetailView
from django.views.generic.list import ListView, BaseListView
from django.views.generic.edit import CreateView
from django_filters.views import FilterView
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.list import MultipleObjectTemplateResponseMixin
from django.core.mail import send_mail, mail_managers
from .models import Good, Tag, Order, GoodFilter, OrderForm


class Index(FilterView):
    model = Good
    filterset_class = GoodFilter
    paginate_by = 5

    def get_page_link(self):
        price_gte = self.request.GET.get('price_gte', '')
        price_lte = self.request.GET.get('price_lte', '')
        name = self.request.GET.get('name', '')
        return ''.join(['name=', name, '&price_gte=', price_gte, '&price_lte=', price_lte, '&'])

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['all_tags'] = Tag.objects.all()
        context['page_link'] = self.get_page_link()
        return context


class GoodDetailView(DetailView):
    model = Good


class TagView(ListView, BaseDetailView):
    model = Tag
    context_object_name = 'current_tag'
    slug_field = 'slug'
    paginate_by = 5
    template_name = 'catalog/good_filter.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(Tag.objects.all())
        return super(TagView , self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.good_set.all()

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        context['all_tags'] = Tag.objects.all()
        context['current_tag'] = self.object
        return context


class OrderView(CreateView):
    form_class = OrderForm
    template_name = 'catalog/order.html'
    success_url = '/catalog/ordered'
    model = Good

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context['good'] = self.get_object(queryset=None)
        return context

    def form_valid(self, form):
        validate_obj = form.save()
        validate_obj.goods.add(self.get_object(queryset=None))
        validate_obj.save()

        recipient = validate_obj.email
        orders_number = str(validate_obj.id)
        message_to_customer = ' '.join(['Уважаемый клиент! Ваш заказ под номером', orders_number, 'поступил в обработку.'])
        message_to_manager = 'Поступил новый заказ.'

        send_mail('Подтверждение заказа', message_to_customer,
            'dariya.grishina@gmail.com', [recipient], fail_silently=False)

        mail_managers(u'Заказ', message_to_manager, fail_silently=False)

        return super(OrderView, self).form_valid(form)
