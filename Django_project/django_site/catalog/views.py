from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the catalog index.")
# Create your views here.

def detail(request, item_id):
    return HttpResponse("You're looking at item %s." % item_id)

def price(request, item_id):
    response = "You're looking at the price of item %s."
    return HttpResponse(response % item_id)

def stock_check(request, item_id):
    return HttpResponse("You're looking on stock %s." % item_id)
