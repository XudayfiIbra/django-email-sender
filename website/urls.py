from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name="register"),
    path('sucsess', views.success, name="success"),
]
