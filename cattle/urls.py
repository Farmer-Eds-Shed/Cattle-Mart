from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_cattle, name='cattle'),
    path('<int:cattle_id>/', views.cattle_detail, name='cattle_detail'),
    path('add/', views.add_cattle, name='add_cattle'),
]