from django.shortcuts import render
from django.http import HttpResponse
import random


def index(request):
    a = random.randrange(1000, 9999, 1)
    return HttpResponse("Hello your code is: " + str(a))


def code(request):
    a = random.randrange(1000, 9999, 1)
    data = {"message": str(a)}
    return render(request, "code1.html", context=data)

