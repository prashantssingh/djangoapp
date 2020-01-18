from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, contact_id):
    return HttpResponse("You're looking at contact %s." % contact_id)
