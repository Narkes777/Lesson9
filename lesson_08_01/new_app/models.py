from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS = (('p', 'Опубликовано'),
              ('d', 'Предварительная версия'),
              ('h', 'Спрятан'))

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS, default='p')
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

