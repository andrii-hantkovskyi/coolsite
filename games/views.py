# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from games.forms import AddGameForm, EditGameForm
from games.mixins import DataMixin
from games.models import Game


class GameList(DataMixin, ListView):
    model = Game
    template_name = 'games/home.html'
    context_object_name = 'games'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GameList, self).get_context_data()
        c_def = self.get_user_context(active_item='home')
        return context | c_def

    def get_queryset(self):
        return Game.objects.filter(in_archive=False)[:5]


class CategoryGames(DataMixin, ListView):
    model = Game
    template_name = 'games/home.html'
    context_object_name = 'games'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryGames, self).get_context_data()
        c_def = self.get_user_context(active_item='categories')
        return context | c_def

    def get_queryset(self):
        return Game.objects.filter(category__slug=self.kwargs['category_slug'], in_archive=False)


class GameDetail(DataMixin, DetailView):
    model = Game
    template_name = 'games/game.html'
    context_object_name = 'game'
    slug_url_kwarg = 'game_slug'

    def get_context_data(self, **kwargs):
        context = super(GameDetail, self).get_context_data()
        c_def = self.get_user_context()
        return context | c_def


class AddGame(DataMixin, CreateView):
    template_name = 'games/add_game.html'
    form_class = AddGameForm

    def get_context_data(self, **kwargs):
        context = super(AddGame, self).get_context_data()
        c_def = self.get_user_context(active_item='add_game')
        return context | c_def


class EditGame(UpdateView):
    model = Game
    template_name = 'games/edit_game.html'
    form_class = EditGameForm
    slug_url_kwarg = 'game_slug'
    context_object_name = 'game'

    def get_queryset(self):
        return Game.objects.filter(slug=self.kwargs['game_slug'])


class DeleteGame(DeleteView):
    model = Game
    slug_url_kwarg = 'game_slug'
    template_name = 'games/delete_game.html'
    success_url = '/'

    def get_queryset(self):
        return Game.objects.filter(slug=self.kwargs['game_slug'])
