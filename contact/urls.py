from . import views
from django.urls import path


urlpatterns = [
    path('', views.feedback, name='contact'),
]
