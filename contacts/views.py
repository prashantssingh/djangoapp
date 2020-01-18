from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. Contact app using Django")

def detail(request, contact_id):
    return HttpResponse("You're looking at contact %s." % contact_id)
