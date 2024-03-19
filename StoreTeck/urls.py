from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Define a URL pattern for the home page
    # Add more URL patterns as needed
]
