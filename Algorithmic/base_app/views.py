from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def welcome_site(request):
    template = loader.get_template('welcome.html')
    return HttpResponse(template.render())
