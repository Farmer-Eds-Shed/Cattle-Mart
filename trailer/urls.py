from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_trailer, name='view_trailer'),
    path('add/<cattle_id>/', views.add_to_trailer, name='add_to_trailer'),
    path('remove/<cattle_id>/', views.remove_from_trailer, name='remove_from_trailer'),
]
