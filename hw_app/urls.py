from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', views.get_all_products, name='products'),
    path('get_product/<int:pk>', views.get_product, name='get_product'),
    path('get_client/<int:pk>', views.get_client, name='get_client'),
    path('get_order/<int:pk>', views.get_order, name='get_order'),

]
