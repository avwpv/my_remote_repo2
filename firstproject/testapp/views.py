from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    s = '<h1> Dont feel difficult .. Just first time filling hard but Really django is very easy  !!!</h1>'
    return HttpResponse(s)
