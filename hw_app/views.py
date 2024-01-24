from django.shortcuts import render
from django.http import HttpResponse
import logging
from . models import Client, Product, Order
from django.core.files.storage import FileSystemStorage
from . forms import ImageForm, ProductEditForm
import datetime
import pytz

utc = pytz.UTC
logger = logging.getLogger(__name__)

# Homework 1


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

# Homework 2


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
    # html = f"""
    # <body bgcolor="LightCyan">
    #     <h1>Selected product</h1>
    #     { product }
    # </body>
    # """

    # return (HttpResponse(html))
    return render(request, template_name='hw_app/product_card.html', context={'product': product})


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
    products = order.products.get()
    html = f"""
    <body bgcolor="LightCyan">
        <h1>Selected order</h1>
        { order }
        { products }
    </body>
    """

    return (HttpResponse(html))

# Homework 3
# Задание №7
# Доработаем задачу 8 из прошлого семинара про клиентов, товары и заказы.
# Создайте шаблон для вывода всех заказов клиента и
# списком товаров внутри каждого заказа.
# Подготовьте необходимый маршрут и представление.


def get_all_clients_orders(request, pk):
    client = Client.objects.filter(pk=int(pk)).first()
    orders = Order.objects.filter(customer=client).all()

    logger.info("Page about client's orders accessed")
    return render(request, template_name='hw_app/order.html', context={'orders': orders, 'client': client, })


def get_all_order_products(request, pk):
    order = Order.objects.filter(pk=int(pk)).first()
    products = order.products.all()

    logger.info("Page about products in the order accessed")
    return render(request, template_name='hw_app/products.html', context={'order': order, 'products': products, })


# Домашнее задание
# Продолжаем работать с товарами и заказами.
# Создайте шаблон, который выводит список заказанных
# клиентом товаров из всех его заказов с сортировкой по времени:
# ○ за последние 7 дней (неделю)
# ○ за последние 30 дней (месяц)
# ○ за последние 365 дней (год)
# *Товары в списке не должны повторятся.
def get_all_client_products(request, client_id, days_num):

    client = Client.objects.filter(pk=int(client_id)).first()
    orders = Order.objects.filter(customer=client).all()
    total_products_list = list()
    for order in orders:
        start_time = datetime.datetime.now().replace(
            tzinfo=utc) - datetime.timedelta(days=days_num)
        end_time = datetime.datetime.now().replace(tzinfo=utc)
        if start_time <= order.order_date.replace(tzinfo=utc) <= end_time:
            products = order.products.all()
            for product in products:
                if product not in total_products_list:
                    total_products_list.append(product)

    logger.info("Page about products ever ordered accessed")
    return render(request, template_name='hw_app/all_client_products.html',
                  context={'client': client, 'total_products_list': total_products_list, 'days_num': days_num, 'start_time': start_time})

# Homework 4
# Задание №6
# Доработаем задачу про клиентов, заказы и товары из
# прошлого семинара.
# Создайте форму для редактирования товаров в базе данных.


def update_product(request):
    if request.method == 'POST':
        form = ProductEditForm(request.POST)
        message = 'Data error'
        if form.is_valid():
            product = form.cleaned_data['product']
            prod_name = product.name
            product_to_edit = Product.objects.filter(name=prod_name).first()

            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']

            product_to_edit.name = name
            product_to_edit.description = description
            product_to_edit.price = price
            product_to_edit.quantity = quantity

            product_to_edit.save()
            message = 'Product updated'
            logger.info(f"Product {product_to_edit} updated")

    else:
        form = ProductEditForm()
        message = 'Fill the form'
        logger.info("Page about updating product accessed")

    return render(request, 'hw_app/update_product.html', {'form': form, 'message': message})


# Задание
# Измените модель продукта, добавьте поле для хранения фотографии продукта.
# Создайте форму, которая позволит сохранять фото.
def upload_image(request, product_id):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product.objects.filter(pk=product_id).first()
            image = form.cleaned_data['image']
            fs = FileSystemStorage()

            product.image_field = fs.save(image.name, image)
            product.save()
            logger.info("Image saved")
    else:
        form = ImageForm()
        logger.info("Page about uploading image accessed")
    return render(request, 'hw_app/upload_image.html', {'form': form})
