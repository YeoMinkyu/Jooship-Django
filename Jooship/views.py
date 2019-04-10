from django.shortcuts import render
from django.views.generic import TemplateView

from . import plots


# Create your views here.
class IndexView(TemplateView):
    template_name = 'Jooship/index.html'


class DetailView(TemplateView):
    template_name = 'Jooship/detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetailView, self).get_context_data(**kwargs)
        context['revenue_plot'] = plots.get_revenue_plot()
        context['cash_flow_plot'] = plots.get_cash_flow_plot()
        context['eps_plot'] = plots.get_eps_plot()
        context['dividends_plot'] = plots.get_dividends_plot()
        return context


def search_ticker(request):
    ticker = request.POST.get('ticker', False)
    print(ticker)
    return render(request, 'Jooship/detail.html')

# class SearchView(TemplateView):
#     pass
