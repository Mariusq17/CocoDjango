from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.controlPanel, name='controlPanel'),
    path('profile/', views.viewProfile, name='profilePage'),
]