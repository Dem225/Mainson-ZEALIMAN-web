from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from boutique.models import Produit
from boutique.panier import Panier


# Create your views here.


def acceuil_veiw(request):
    produit=Produit.objects.filter(disponible=True)
    context={
        'produit' : produit
    }
    return render( request, "boutique/accueil.html",context)


def detail_produit(request, slug):
    produit=get_object_or_404(Produit,slug=slug)
    context={
        'produit':produit
    }
    return render(request,  "boutique/detail_produit.html",context)  




def acceuil_veiw(request):
    produit = Produit.objects.filter(disponible=True)
    context = {'produit': produit}
    return render(request, "boutique/accueil.html", context)

def detail_produit(request, slug):
    produit = get_object_or_404(Produit, slug=slug)
    context = {'produit': produit}
    return render(request, "boutique/detail_produit.html", context)

def ajouter_au_panier(request, slug):
    produit=get_object_or_404(Produit, slug=slug)
    panier=Panier(request)
    panier.ajouter(produit)
    return redirect('voir_panier')
    

def voir_panier(request):
    panier=Panier(request)
    context={
        'panier' : panier
    }
    return render(request,"boutique/panier.html",context )
