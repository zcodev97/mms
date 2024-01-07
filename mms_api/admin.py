from django.contrib import admin
from .models import InvoiceType, Invoice, Client, Container


# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'total', 'created_at']


@admin.register(InvoiceType)
class InvoiceTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'invoice_id', 'company_name', 'invoice_type', 'created_at',
                    'mr', 'price_in_dinar', 'price_in_dollar',
                    'description', 'accounter', 'receiver']
