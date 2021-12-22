from django.contrib import admin
# Register your models here.
from django.contrib.admin import ModelAdmin

from .models import *


@admin.register(GameCategory)
class GameCategoryAdmin(ModelAdmin):
    fields = ('slug', 'name')


@admin.register(Game)
class GameAdmin(ModelAdmin):
    fields = ('category', 'name', 'slug', 'content', 'image', 'in_archive')
    list_display = ('id', 'name', 'in_archive')
    list_editable = ('in_archive',)
