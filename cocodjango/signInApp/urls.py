from django.urls import path
from . import views

urlpatterns = [
    path("", views.formPage, name="formPage"),
    path("logout/", views.update_last_online, name='logoutUser'),
    path("resetPassword/", views.resetPasswordFormPage, name="resetPassword"),
]