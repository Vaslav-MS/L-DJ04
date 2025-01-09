from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Это мой первый проект на Django</h1>')

def new(request):
    return HttpResponse('<h1>Это вторая страница</h1>')

def data(request):
    return HttpResponse('<h1>Это страница DATA</h1>')

def test(request):
    return HttpResponse('<h1>Это страница TEST</h1>')

