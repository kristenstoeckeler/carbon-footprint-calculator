from django.urls import path
from users import views as users_views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'users'

# KRISTEN: UNSURE IF WE WILL NEED ALL THESE
urlpatterns = [
    path('', users_views.index, name='home'),
    path('', users_views.index.as_view(), name='home'),
    path('api/users/', users_views.user_list),
    path('api/users/<int:pk>/', users_views.user_detail),
    path('api/users/published/', users_views.user_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)