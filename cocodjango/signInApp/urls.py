from django.urls import path
from . import views

urlpatterns = [
    path("", views.formPage, name="formPage"),
]