from django.contrib import admin
from django.urls import path
from brands.views import BrandsListView, BrandDeleteView, create_brand, update_brand


urlpatterns = [
    path('brand-list/', BrandsListView.as_view(), name='brand-list'),
    path('brand-create/', create_brand, name='brand-create'),
    path('brand-update/<int:pk>/', update_brand, name='brand-update'),
    path('brand-delete/<int:pk>/', BrandDeleteView.as_view(), name='brand-delete'),

]