# from http.client import HTTPResponse
from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
# request -> response

def say_hello(request):
    # pull data from DB
    # Transform
    # Send email
    x = 1
    y = 2

    return render(request, 'hello.html', {'name': 'Carlos Alvarado Villegas'})
    

