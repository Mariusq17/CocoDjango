from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("form", views.formMain, name="form"),
    path("form/1", views.form1, name="form1"),
    path("form/2", views.form2, name="form2"),
    path("form/3", views.form3, name="form3"),
]