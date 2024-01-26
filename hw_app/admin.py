from django.contrib import admin
from .models import Client, Product, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'telephone']
    ordering = ['name', 'address']
    list_filter = ['name', 'address']
    search_fields = ['name']
    search_help_text = 'Search by the name of a client'

    readonly_fields = ['birthday']

    fieldsets = [
        (
            'Client',
            {
                'classes': ['wide'],
                'fields': ['name', 'email'],
            },
        ),
        (
            'Contact details',
            {
                'classes': ['collapse'],
                'description': 'Contact information',
                'fields': ['telephone', 'address'],
            },
        ),
        (
            'Other info',
            {
                'description': 'Other information',
                'fields': ['birthday'],
            }
        ),
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    ordering = ['name', 'quantity']
    list_filter = ['name', 'price']
    search_fields = ['name']
    search_help_text = 'Search by the name of a product'

    readonly_fields = ['image_field']

    fieldsets = [
        (
            'Client',
            {
                'classes': ['wide'],
                'fields': ['name', 'price'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description': 'Details',
                'fields': ['description', 'image_field'],
            },
        ),
        (
            'Other info',
            {
                'description': 'Other information',
                'fields': ['quantity', 'receipt_date'],
            }
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'order_date', 'total_price',]
    ordering = ['-order_date']
    list_filter = ['products', 'order_date']
    search_fields = ['customer']
    search_help_text = 'Search by the name of a client'

    readonly_fields = ['total_price', 'order_date']

    fieldsets = [
        (
            'Order',
            {
                'classes': ['wide'],
                'fields': ['customer', 'order_date', 'total_price'],
            },
        ),
        (
            'Products',
            {
                'classes': ['collapse'],
                'description': 'Products ordered',
                'fields': ['products'],
            },
        ),
    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
