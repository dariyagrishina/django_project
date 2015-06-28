from django.contrib import admin

from .models import Good, Tag, Order, OrderedGood


class GoodsInline(admin.TabularInline):
    model = OrderedGood
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'address', 'handle_order')
    list_filter = ['handle_order']
    list_editable = ['handle_order']

    inlines = [
        GoodsInline,
    ]

admin.site.register(Good)
admin.site.register(Tag)
admin.site.register(Order, OrderAdmin)
