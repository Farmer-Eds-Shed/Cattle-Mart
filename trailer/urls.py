from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_trailer, name='view_trailer'),
    path('add/<cattle_id>/', views.add_to_trailer, name='add_to_trailer'),
]