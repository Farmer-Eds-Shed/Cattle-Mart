from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_trailer, name='view_trailer')
]