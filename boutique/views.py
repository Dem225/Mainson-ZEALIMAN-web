from django.shortcuts import render
from boutique.models import Produit
# Create your views here.


def acceuil_veiw(request):
    produit=Produit.objects.filter(disponible=True)
    context={
        'produit' : produit
    }
    return render( request, "boutique/accueil.html",context)