from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'fsdfsdf435'})


def password(request):

    charactesrs = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        charactesrs.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        charactesrs.extend(list('0123456789'))

    if request.GET.get('special'):
        charactesrs.extend(list('!@#$%^&*()'))

    lenght = int(request.GET.get('lenght', 12))

        


    thepassword = ''

    for x in range(lenght):
        thepassword += random.choice(charactesrs)

    return render(request, 'generator/password.html', {'password':thepassword})


def about(request):
    return render(request, 'generator/about.html')
    

