from django.urls import path
from users.views import login_view, login_success, signup
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html')),
    path('login-success/', login_success, name='login_success'),
    path('signup/', signup, name='signup'),


]