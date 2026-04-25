from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from users import views as users_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', RedirectView.as_view(url='/footprints/', permanent=False), name='home'),
    path('register/', users_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('api/users/', users_views.user_list, name='user_list'),
    path('api/users/<int:user_id>/choices/', users_views.user_choices, name='user_choices'),
    path('api/users/<int:user_id>/total-footprint/', users_views.user_total_footprint, name='user_total_footprint'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)