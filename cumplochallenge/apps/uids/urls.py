from django.urls import path
from apps.uids.views import index, exchange_rate, international_reserves, interest_rates, udis

urlpatterns = [
    path('', index),
    path('international_reserves', international_reserves),
    path('interest_rates', interest_rates),
    path('exchange_rate', exchange_rate),
    path('udis', udis),
]