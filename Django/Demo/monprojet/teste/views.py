from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def teste(request, name=None):
    return render(request, "teste.html", {'name' : name})

def testet(request, name=None):
    return HttpResponse(f" Salut {name} !!")