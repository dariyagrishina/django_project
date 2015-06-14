# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import Good, Tag, Order, GoodFilter, OrderForm


class Index(ListView):
    model = Good
    paginate_by = 5

    def get_queryset(self):
        queryset = super(Index, self).get_queryset()
        self.f = GoodFilter(self.request.GET, queryset=queryset)

        return self.f.qs

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['all_tags'] = Tag.objects.all()
        context['filter'] = self.f

        price_gte = self.request.GET.get('price_gte', '')
        price_lte = self.request.GET.get('price_lte', '')
        name = self.request.GET.get('name', '')
        context['page_link'] = ''.join(['name=', name, '&price_gte=', price_gte, '&price_lte=', price_lte, '&'])

        return context


class GoodDetailView(DetailView):
    model = Good


class TagView(ListView):
    model = Good
    paginate_by = 5

    def dispatch(self, request, slug=None):
        self.current_tag = get_object_or_404(Tag, slug=slug)
        return super(TagView, self).dispatch(request, slug=slug)

    def get_queryset(self):
        tags_goods = self.current_tag.good_set.all()
        return tags_goods

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        context['all_tags'] = Tag.objects.all()
        context['current_tag'] = self.current_tag
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
        return super(CreateView, self).form_valid(form)
