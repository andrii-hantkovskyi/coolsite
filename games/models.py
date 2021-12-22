from django.db import models

# Create your models here.
from django.urls import reverse


class GameCategory(models.Model):
    slug = models.SlugField(max_length=50, unique=True)
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Game categories'


class Game(models.Model):
    category = models.ForeignKey(GameCategory, on_delete=models.CASCADE, verbose_name='Category')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')
    name = models.CharField(max_length=50, verbose_name='Name')
    content = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='images/%Y/%m/%d', default='None/no-image.png', verbose_name='Image')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Publication date')
    last_update = models.DateTimeField(auto_now=True, verbose_name='Last updated')
    in_archive = models.BooleanField(default=False, verbose_name='In archive')

    def get_absolute_url(self):
        return reverse('game', kwargs={'game_slug': self.slug})

    def __str__(self):
        return self.name
