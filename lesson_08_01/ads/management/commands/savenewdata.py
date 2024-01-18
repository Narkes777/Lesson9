from django.core.management.base import BaseCommand
from ads.models import Author, Ad, Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        new_ad = Ad.objects.create(name="Ad from custom command", author=author) # foreign key
        new_ad.author = author # foreign key
        new_ad.save()
        cat = Category.objects.create(name='Category from command')
        new_ad.category.add(cat)
