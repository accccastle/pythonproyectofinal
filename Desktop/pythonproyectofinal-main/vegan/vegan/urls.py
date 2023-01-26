from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from vegan.views import index, about

urlpatterns = [
    path('',index, name='index'),
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('market/', include('market.urls')),
    path('brands/', include('brands.urls')),
    path('users/', include('users.urls')),
]
