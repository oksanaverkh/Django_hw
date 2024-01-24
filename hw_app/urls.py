from django.urls import path
from . import views

urlpatterns = [
    # Homework 1
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # Homework 2
    path('products/', views.get_all_products, name='products'),
    path('get_product/<int:pk>', views.get_product, name='get_product'),
    path('get_client/<int:pk>', views.get_client, name='get_client'),
    path('get_order/<int:pk>', views.get_order, name='get_order'),
    # Homework 3
    path('get_clients_orders/<int:pk>',
         views.get_all_clients_orders, name='get_clients_orders'),
    path('get_order_products/<int:pk>',
         views.get_all_order_products, name='get_order_products'),
    path('get_all_client_products/<int:client_id>/<int:days_num>',
         views.get_all_client_products, name='get_all_client_products'),
    # Homework 4
    path('upload_image/<int:product_id>',
         views.upload_image, name='upload_image'),
    path('update_product/', views.update_product, name='update_product'),
]
