from games.models import GameCategory


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['categories'] = GameCategory.objects.all()
        return context
