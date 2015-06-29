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
from cart import Cart
from .models import Good, Tag, Order, GoodFilter, OrderForm, OrderedGood
from django.template import RequestContext
from context_processors import cart



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


def detail(request, pk):
    good = get_object_or_404(Good, pk=pk)
    context = dict(cart=Cart(request))
    return render(request, 'catalog/good_detail.html', {"good": good})

def add_item(request, pk):
    good = get_object_or_404(Good, pk=pk)
    cart = Cart(request)
    cart.add(good, good.price, 1)
    url = request.GET.get('url')

    return HttpResponseRedirect(url)

def remove_item(request, pk):
    good = get_object_or_404(Good, pk=pk)
    url = request.GET.get('url')
    cart = Cart(request)
    cart.remove(good)
    return HttpResponseRedirect(url)


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

    def form_valid(self, form):
        validate_obj = form.save()
        cart = Cart(self.request)
        for item in Cart(self.request):
            ordered = OrderedGood.objects.create(order=validate_obj, good=item.product, quantity=item.quantity)
            cart.remove(item.product)

        return super(OrderView, self).form_valid(form)
