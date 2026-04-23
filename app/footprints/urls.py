from django.urls import path
from . import views

app_name = 'footprints'

urlpatterns = [
    path('api/lifestyles/', views.lifestyle_list, name='lifestyle_list'),
    path('api/choices/', views.choice_list, name='choice_list'),
    path('api/choices/<int:id>/', views.choice_detail, name='choice_detail'),
    path('', views.index.as_view(), name='index'),
    path('footprints/', views.list_all_footprints.as_view(), name='list_all_footprints'),
]
