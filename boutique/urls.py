
from boutique.views import *
from django.urls import path
urlpatterns = [
   path('',acceuil_veiw, name='home' ) ,
   path('detail_produit/<slug:slug>/',detail_produit, name='detail_produit' ) ,
   path('ajouter_au_panier/<slug:slug>/',ajouter_au_panier, name='ajouter_au_panier' ) ,
   path('voir_panier/',voir_panier, name='voir_panier' ) ,

]
