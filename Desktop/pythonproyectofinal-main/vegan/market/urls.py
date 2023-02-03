from django.urls import path
from market.views import create_market, create_location, create_resto, MarketListView, LocationtListView, RestoListView, \
    update_market, update_resto, update_location, RestoDeleteView, MarketDeleteView, LocationDeleteView


urlpatterns = [
    path('market-formulario/', create_market, name='create_market'),
    path('market-list/', MarketListView.as_view(), name='list_market'),
    path('market-update/<int:pk>/', update_market, name='update_market'),
    path('market-delete/<int:pk>/', MarketDeleteView.as_view(), name='delete-market'),
    path('resto-formulario/', create_resto, name='create_resto'),
    path('resto-list/', RestoListView.as_view(), name='list_resto'),
    path('resto-update/<int:pk>/', update_resto, name='update-resto'),
    path('resto-delete/<int:pk>/', RestoDeleteView.as_view(), name='delte-resto'),
    path('location-formulario/', create_location, name='create-location'),
    path('location-list/', LocationtListView.as_view(), name='list-location'),
    path('location-update/<int:pk>/', update_location, name='update-location'),
    path('location-delete/<int:pk>/', LocationDeleteView.as_view(), name='delete-location'),     
]


