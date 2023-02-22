from django.contrib import admin

# Register your models here.
from menu_app.models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'url', 'name')
    list_filter = ('name',)

admin.site.register(MenuItem, MenuItemAdmin)