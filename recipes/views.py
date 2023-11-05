from django.shortcuts import render
from django.http import HttpResponse


def _home(request):
    return HttpResponse("HOME 1")

def _contato(request):
    return HttpResponse('Contato')

def _sobre(request):
    return HttpResponse('Sobre')