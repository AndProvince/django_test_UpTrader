from django.urls import path

from . import views

urlpatterns = [
    # например: /menu/
    path('', views.index, name='index'),
    # например: /menu/5/
    path('<int:menu_id>/', views.detail, name='detail'),
]