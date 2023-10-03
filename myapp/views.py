from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    html = "<h1>Hello, world!</h1>" \
           "<p>Домашнее задание №1</p>" \
           "<p>Создайте пару представлений в вашем первом приложении:" \
           "<br>— главная" \
           "<br>— о себе." \
           "<br>Внутри каждого представления должна быть переменная html — многострочный текст" \
           " с HTML-вёрсткой и данными о вашем первом Django-сайте и о вас." \
           "Сохраняйте в логи данные о посещении страниц.</p>"

    logger.info(f'Показана информация: {html}')
    return HttpResponse(html)
def about(request):
    html = "<h1>About us</h1>" \
           "<p>Страница о нас</p>"
    logger.info(f'Показана информация: {html}')
    return HttpResponse(html)

