from django.urls import path

from .views import GameList, CategoryGames, GameDetail, AddGame, EditGame, DeleteGame

urlpatterns = [
    path('', GameList.as_view(), name='home'),
    path('category/<slug:category_slug>/', CategoryGames.as_view(), name='category'),
    path('game/<slug:game_slug>', GameDetail.as_view(), name='game'),
    path('add-game/', AddGame.as_view(), name='add-game'),
    path('edit-game/<slug:game_slug>/', EditGame.as_view(), name='edit-game'),
    path('delete-game/<slug:game_slug>/', DeleteGame.as_view(), name='delete-game')
]
