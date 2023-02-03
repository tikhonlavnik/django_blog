from .models import *


categories = Category.objects.all()


class DataMixin:
    paginate_by = 5

    def get_user_context(self, **kwargs):
        context = kwargs
        context['categories'] = categories
        return context
