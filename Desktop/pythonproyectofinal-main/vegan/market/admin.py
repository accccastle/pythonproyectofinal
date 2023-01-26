from django.contrib import admin
from market.models import Restaurants, Location, Market

@admin.register(Restaurants)
class RestaurantsAdmin(admin.ModelAdmin):
    list_display = ('name','location','food_type')
    
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('locationame','type_shop','name_shop')
    
@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = ('name_market','name_product','location','price')


