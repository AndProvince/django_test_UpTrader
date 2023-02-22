from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import MenuItem

# Create your views here.
# Вьюха для базовой страницы приложения
def index(request):
    message = "Привет, сейчас ничего не выбрано из меню"
    return render(request, 'index.html', {'message': message, 'current_url': request.path})

# Вьюха для выбранного пункта меню
def detail(request, menu_id):
    # Находим выбранный пункт меню в БД
    menu_items = MenuItem.objects.filter(id=menu_id)

    # Формируем сообщения для отображения на странице
    message = "Выбрано меню - %s." % menu_items[0].title

    # Находим родительский пункт меню если он есть - для отображения раскрытого меню от уровня родителя
    if menu_items[0].parent:
        current_url = menu_items[0].parent.url
    else:
        current_url = menu_items[0].url

    return render(request, 'index.html', {'message': message, 'current_url': current_url})