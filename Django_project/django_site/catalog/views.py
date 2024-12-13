"""This file contains all views

All functions returns a http response to the navigator.
Links python and html files
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, Commission
from catalog.forms import CommissionForm
# Create your views here.

def index(request):
    """Default page of the app.
    Args:
        request (HttpRequest): The demand of the user by url
    Returns:
        HttpResponse: renders the template "index.html" with information from the database.
    """
    items = Item.objects.all()
    commissions = Commission.objects.all()
    return render(request, "index.html", {'items': items, 'commissions': commissions})

def detail(request, item_id):
    """Displays information on a chosen item

    :param request: Request made by a user via url
    :type request: HttpRequest
    :return: Returns the template "item_detail.html" with item information
    :rtype: HttpResponse
    """    
    context = Item.objects.get(id=item_id)
    return render (request, "item_detail.html", {"item_object" : context})

def stock_check(request, item_id):
        # A ameliorer en affichage de tous les détails du stock
    return HttpResponse("You're looking on stock %s." % item_id)

def info_commission(request, commission_id):
    """Displays information on a chosen commission

    :param request: Request made by a user via url
    :type request: HttpRequest
    :param commission_id: Id number of of the commission 
    :type commission_id: Int
    :return: Returns the template "commission_detail.html" with item information
    :rtype: HttpResponse
    """    
    context = Commission.objects.get(id=commission_id)
    return render (request, "commission_detail.html", {"commission_object" : context})

def commission_create(request):
    """ Displays a form page to complete
    On completion, adds the commission object to the database
    and redirects to the index
    
    :param request: Request made by a user via url
    :type request: HttpRequest
    :return: Returns the template "commission_create.html" on get and "index.html" on post
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        form = CommissionForm(request.POST)
        if form.is_valid():
            # create a new commission object and save it to the database
            commission = form.save()
            return redirect('index')
    else:    
        form = CommissionForm()
    return render(request, 
        'commission_create.html', 
        {'form': form})
    
