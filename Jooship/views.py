from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

from . import plots

# Create your views here.
class IndexView(TemplateView):
    template_name = 'Jooship/index.html'

class DetailView(TemplateView):
    template_name = 'Jooship/detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetailView, self).get_context_data(**kwargs)
        context['plot'] = plots.get_graph()
        return context
