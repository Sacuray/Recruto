from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello " + request.GET["name"] + "! " + request.GET["message"].replace("%", " ") + "!")