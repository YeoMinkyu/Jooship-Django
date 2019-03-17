from django.urls import path

from .views import IndexView, DetailView

app_name = 'Jooship'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<str:stock_ticker>', DetailView.as_view(), name='detail'),
]