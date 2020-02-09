from django.urls import path

from .views import IndexView, DetailView, search_ticker

app_name = 'Jooship'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<str:stock_ticker>', DetailView.as_view(), name='detail'),
    path('search/', search_ticker, name='search')
    # path('/search/<str:stock_ticker>', SearchView.as_view(), name='search'),
]

# End of File
