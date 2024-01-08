from django.db import models

# Create your models here.


class Ad(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя рекламы")
    content = models.TextField(null=True, blank=True, verbose_name="Содержание рекламы")
    price = models.FloatField(null=True, blank=True, verbose_name="Цена")
    published = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Рекламы"

    def __str__(self):
        return str(self.price)
