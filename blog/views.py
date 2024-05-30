from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.template import loader


def home(request):
    template = loader.get_template('home.html').render()
    return HttpResponse(template)


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())


def contact(request):
    template = loader.get_template('contact.html').render()
    return HttpResponse(template)
