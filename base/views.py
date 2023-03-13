from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tasksList(request):
    return HttpResponse('To do list')