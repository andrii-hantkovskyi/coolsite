from django.forms import ModelForm

from games.models import Game


class AddGameForm(ModelForm):
    class Meta:
        model = Game
        fields = ('category', 'name', 'slug', 'content', 'image', 'in_archive')


class EditGameForm(ModelForm):
    class Meta:
        model = Game
        fields = ('content',)

