from django import template
from menu_app.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    # Получаем из БД меню которое необходимо отобразить, корень - menu_name
    menu_items = MenuItem.objects.filter(name=menu_name)

    # Сортируем пункты меню по порядку
    menu_items = menu_items.order_by('parent')

    # Создаем пустой список, в который будем добавлять словари с информацией о пунктах меню
    menu_data = []

    # Проходимся по всем пунктам меню
    for item in menu_items:
        # Создаем словарь с информацией о текущем пункте меню
        item_data = {
            'id': item.id,
            'title': item.title,
            'url': item.url,
            'children': []
        }

        # Если у текущего пункта есть родитель, добавляем его в список дочерних пунктов родительского пункта
        if item.parent:
            for parent_data in menu_data:
                if parent_data['id'] == item.parent.id:
                    parent_data['children'].append(item_data)
                    break
        # Иначе добавляем его в основной список пунктов меню
        else:
            menu_data.append(item_data)

    return {'menu_data': menu_data, 'current_url': context['current_url']}
