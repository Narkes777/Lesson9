from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Ad(models.Model):
    STATUSES = ((None, 'Выберите статус рекламы'),
                ('s', 'Продано'),
                ('a', 'Активна'),
                ('c', 'Отменена'))


    # CASCADE
    # SET (Ставит переданное значение)
    # SET_DEFAULT - ставит значени по умолчанию
    # SET_NULL - ставит None
    # PROTECT - не дает удалить первичную модель
    name = models.CharField(max_length=50, verbose_name="Имя рекламы", help_text='Здесь заполняется имя рекламы', default='Имя по умолчанию', unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, related_name='ads') # default related_name = <название модели>_set
    category = models.ManyToManyField('Category')
    is_active = models.BooleanField(null=True, blank=True) # None
    status = models.CharField(max_length=1, choices=STATUSES, default='a', verbose_name='Статус рекламы')
    content = models.TextField(null=True, blank=True, verbose_name="Содержание рекламы", unique_for_year='published')
    price = models.FloatField(null=True, blank=True, verbose_name="Цена")
    published = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Рекламы"
        ordering = ['price']
        # unique_together = (('name', 'price'))
        # get_latest_by = 'price' Ad.objects.last()

    def __str__(self):
        return self.name + ' ' + str(self.price)


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name




# class TestModel(models.Model):
#     name = models.CharField(max_length=100) # обязательный аттрибут max_length
#     content = models.TextField()
#     email = models.EmailField()
#     url = models.URLField()
#     is_active = models.BooleanField()
#     is_member = models.NullBooleanField()
#     price = models.IntegerField()
#     code = models.BigIntegerField()
#     id = models.SmallIntegerField()
#     discounted_price = models.PositiveIntegerField()
#     discount = models.FloatField()
#     new_price = models.DecimalField(max_digits=10, decimal_places=2)
#     date_of_issue = models.DateField(auto_now_add=True)
#     published = models.DateTimeField(auto_now=True)
#     time_of_expiration = models.TimeField()
#     bin_code = models.BinaryField()




