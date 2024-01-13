from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Main page accessed')
    html = """
    <body bgcolor="red">
<h1>Это мой первый сайт</h1>
<p>Я никогда не создавала сайты, поэтому он такой непрезентабельный.</p>
</body>
"""
    return HttpResponse(html)


def about(request):
    logger.info('Page about the author accessed')
    html = """
    <body bgcolor="black">
<h1 style="color: white">Привет, меня зовут Oксана</h1>
<p style="color: white">Я никогда не создавала сайты и не работала в IT.<br/>
В университете я изучала С++ и web-разработку, но тогда мне это было не интересно,
 и задания за меня делали случайно найденные в коридоре студенты-айтишники.</p>
<p style="color: white">Как оказалось, это было ошибкой, нужно было учиться.</p>
</body>
"""
    return HttpResponse(html)
