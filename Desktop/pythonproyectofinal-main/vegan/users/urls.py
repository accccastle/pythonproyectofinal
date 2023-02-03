from django.urls import path
from users.views import login_view, login_success, signup, update, update_profile, UserDeleteView, profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html')),
    path('login-success/', login_success, name='login_success'),
    path('signup/', signup, name='signup'),
    path('update/', update, name='update'),
    path('update-profile/', update_profile, name='update_profile'),
    path('profile/', profile, name='profile'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='delete-user'),
]