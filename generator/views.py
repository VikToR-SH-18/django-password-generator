from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'generator/home.html', {'password': 'qwerty12345'})


def description(request):
    return render(request, 'generator/description.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend('1234567890')

    if request.GET.get('special'):
        characters.extend('!@#$%^&*()')

    length = int(request.GET.get('length', 12))

    thepass = ''

    for x in range(length):
        thepass += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepass})
