# Create your views here.
from django.shortcuts import render


# import http response 
from django.http import HttpResponse

# create view as a function
def sayHello(request):
    # when a python object representing an http request is passed into this method, it returns an http response that says hello world
    return HttpResponse('Hello, World!')