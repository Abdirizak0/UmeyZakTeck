from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world!")  # Example response for the home page