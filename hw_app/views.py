from django.shortcuts import render
from django.http import HttpResponse
import logging
from . models import Client, Product, Order

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Main page accessed')
    html = """
    <body bgcolor="LightCyan">
<h1>Добро пожаловать в интернет-магазин!</h1>
<p>Это главная страница.</p>
</body>
"""
    return HttpResponse(html)


def about(request):
    logger.info('Page about the author accessed')
    html = """
    <body bgcolor="Indigo">
<h1 style="color: white">Привет, меня зовут Oксана</h1>
<p style="color: white">Я никогда не создавала сайты и не работала в IT.<br/>
В университете я изучала С++ и web-разработку, но тогда мне это было не интересно,
 и задания за меня делали случайно найденные в коридоре студенты-айтишники.</p>
<p style="color: white">Как оказалось, это было ошибкой, нужно было учиться.</p>
</body>
"""
    return HttpResponse(html)


def get_all_products(request):
    logger.info('Page with all products list accessed')
    products = Product.objects.all()
    result = '<br>'.join([str(product) for product in products])

    html = f"""
    <body bgcolor="LightCyan">
        <h1>List of available products</h1>
        { result }
    </body>
    """

    return (HttpResponse(html))


def get_product(request, pk):
    logger.info('Page about selected product accessed')
    product = Product.objects.filter(pk=int(pk)).first()
    html = f"""
    <body bgcolor="LightCyan">
        <h1>Selected product</h1>
        { product }
    </body>
    """

    return (HttpResponse(html))


def get_client(request, pk):
    logger.info('Page about selected client accessed')
    client = Client.objects.filter(pk=int(pk)).first()
    html = f"""
    <body bgcolor="LightCyan">
        <h1>Selected client</h1>
        { client }
    </body>
    """

    return (HttpResponse(html))

def get_order(request, pk):
    logger.info('Page about selected order accessed')
    order = Order.objects.filter(pk=int(pk)).first()
    html = f"""
    <body bgcolor="LightCyan">
        <h1>Selected order</h1>
        { order }
    </body>
    """

    return (HttpResponse(html))
