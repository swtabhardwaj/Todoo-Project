from django.http import HttpResponse
from django.shortcuts import render

def addTask(request):
    return HttpResponse("This is the addTask view.")
