from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from . import plots


# Create your views here.
class IndexView(TemplateView):
    template_name = 'Jooship/index.html'


class DetailView(TemplateView):
    template_name = 'Jooship/detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DetailView, self).get_context_data(**kwargs)
        ticker = kwargs['stock_ticker']
        print(ticker)
        context['revenue_plot'] = plots.get_revenue_plot()
        context['cash_flow_plot'] = plots.get_cash_flow_plot()
        context['eps_plot'] = plots.get_eps_plot()
        context['dividends_plot'] = plots.get_dividends_plot()
        return context


@csrf_exempt
def search_ticker(request):
    # ticker = request.POST.get('ticker', False)
    try:
        ticker = request.POST.get('ticker', False)
    except KeyError:
        print("error")
        return HttpResponseRedirect(reverse('Jooship:index'))
    else:
        # print(ticker)
        pass
    return HttpResponseRedirect(reverse('Jooship:detail', kwargs={'stock_ticker': ticker}))
# End of File
