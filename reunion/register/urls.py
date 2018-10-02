from django.urls import path
from . import views

urlpatterns = [
    # Paths del register
    path('', views.register, name="register"),
]