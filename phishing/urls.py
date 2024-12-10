from django.urls import path
from . import views
from .views import capture

urlpatterns = [
    path('', views.index, name='index'),
    path('capture/', views.capture, name='capture'),
]