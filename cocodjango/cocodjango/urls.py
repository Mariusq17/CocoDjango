from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("initialState.urls")),
    path("signIn/", include("signInApp.urls")),
    path("controlPanel/", include("userApp.urls")),
]
