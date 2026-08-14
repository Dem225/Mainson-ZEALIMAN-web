from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from boutique.models import Produit
from boutique.panier import Panier
from django.contrib.auth.decorators import login_required
from boutique.panier import Panier
from commandes.models import Commande, LigneCommande


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


def supprimer_du_panier(request, slug):
    produit = get_object_or_404(Produit, slug=slug)
    panier = Panier(request)
    panier.supprimer(produit)
    return redirect('voir_panier')

def modifier_quantite_panier(request, slug):
    produit = get_object_or_404(Produit, slug=slug)
    panier = Panier(request)
    quantite = int(request.POST.get('quantite'))
    panier.modifier_quantite(produit, quantite)
    return redirect('voir_panier')



@login_required
def passer_commande(request):
    panier = Panier(request)

    if request.method == 'POST':
        adresse = request.POST.get('adresse_livraison')
        commande = Commande.objects.create(
            client=request.user, adresse_livraison=adresse, total=panier.get_total()
        )
        for item in panier:
            LigneCommande.objects.create(
                commande=commande,
                produit=item['produit'],
                quantite=item['quantite'],
                prix_unitaire=item['prix']
            )
        panier.vider()
        return redirect('confirmation_commande', commande_id=commande.id)

    context = {'panier': panier}
    return render(request, 'boutique/passer_commande.html', context)




@login_required
def confirmation_commande(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id, client=request.user)
    context = {'commande': commande}
    return render(request, 'boutique/confirmation.html', context)


@login_required
def historique_commandes(request):
    commandes = Commande.objects.filter(client=request.user).order_by('-date_commande')
    context = {'commandes': commandes}
    return render(request, 'boutique/historique.html', context)