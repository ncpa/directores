from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    #path('register/', views.register, name="register"),
    path('about/', views.about, name="about"),
    path('program/', views.program, name="program"),
    path('contact', views.contact, name="contact"),
]