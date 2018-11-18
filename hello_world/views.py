# Create your views here.
from django.shortcuts import render


# import http response 
from django.http import HttpResponse

# import html renderer
from django.shortcuts import render

# create view as a function
def sayHello(request):
    # when a python object representing an http request is passed into this method, it returns an http response that says hello world
    return HttpResponse('Hello, World!')

def sayHelloInHtml(request):
    # this automagically looks under /templates for a view named hello.html
    return render(request, 'hello.html')