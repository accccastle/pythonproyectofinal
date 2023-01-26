from django.urls import path
from market.views import create_market, create_location, create_resto, MarketListView, LocationtListView, RestoListView

urlpatterns = [
    path('market-formulario/', create_market, name='create_market'),
    path('location-formulario/', create_location, name='create_location'),
    path('resto-formulario/', create_resto, name='create_resto'),
    path('market-list/', MarketListView.as_view(), name='list_market'),
    path('resto-list/', RestoListView.as_view(), name='list_resto'),
    path('location-list/', LocationtListView.as_view(), name='list_location'),
           
]


