from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.controlPanel, name='controlPanel'),
    path("logout/", views.update_last_online, name='logoutUser'),
]