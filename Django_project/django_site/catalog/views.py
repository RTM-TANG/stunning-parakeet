from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, Commission
from catalog.forms import CommissionForm
# Create your views here.

def index(request):
    items = Item.objects.all()
    commissions = Commission.objects.all()
    return render(request, "index.html", {'items': items, 'commissions': commissions})

def detail(request, item_id):
    # A ameliorer en affichage de tous les détails de l'item
    return HttpResponse("You're looking at item %s." % item_id)

def stock_check(request, item_id):
        # A ameliorer en affichage de tous les détails du stock
    return HttpResponse("You're looking on stock %s." % item_id)

# créer une page pour détailler les infos d'une commission

def commission_create(request):
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
    
