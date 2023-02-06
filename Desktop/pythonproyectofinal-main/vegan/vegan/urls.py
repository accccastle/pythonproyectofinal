from django.contrib import admin
from django.urls import path, include
from vegan.views import index, about, delete
from vegan.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
from contact.views import contact

urlpatterns = [
    path('',index, name='index'),
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('delete/', delete, name='delete'),
    path('market/', include('market.urls')),
    path('brands/', include('brands.urls')),
    path('users/', include('users.urls')),
    
] + static(MEDIA_URL, document_root = MEDIA_ROOT)

