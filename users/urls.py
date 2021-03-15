from django.urls import path
from . import views

urlpatterns = [
    # pattern will be handled by views.home file
    path('register/', views.register, name="register"),
]
