from django.views.generic import ListView
from models import Menu

class IndexView(ListView):
    queryset = Menu.objects.all()
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['queryset'] = self.queryset
        return context

