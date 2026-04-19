from django.urls import path
from . import views

app_name = 'footprints'

urlpatterns = [
    path('api/footprints/', views.footprint_list, name='footprint_list'),
    path('api/footprints/<int:pk>/', views.footprint_detail, name='footprint_detail'),
    path('api/footprints/published/', views.footprint_list_published, name='footprint_list_published'),
]
