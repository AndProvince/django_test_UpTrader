from django.db import models

# Create your models here.

class MenuItem(models.Model):
    # Модель для хранения меню в БД
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.title
