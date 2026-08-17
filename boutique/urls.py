
from boutique.views import *
from django.urls import path
urlpatterns = [
   path('',acceuil_veiw, name='home' ) ,
   path('detail_produit/<slug:slug>/',detail_produit, name='detail_produit' ) ,
   path('ajouter_au_panier/<slug:slug>/',ajouter_au_panier, name='ajouter_au_panier' ) ,
   path('voir_panier/',voir_panier, name='voir_panier' ) , 
   path('supprimer_du_panier/<slug:slug>/',supprimer_du_panier, name='supprimer_du_panier' ) ,
   path('modifier_quantite_panier/<slug:slug>/',modifier_quantite_panier, name='modifier_quantite_panier' ) ,
   path('passer_commande/', passer_commande, name='passer_commande'),
   path('confirmation_commande/<int:commande_id>/',confirmation_commande, name='confirmation_commande' ) , 
   path('historique_commandes/', historique_commandes, name='historique_commandes'),
   path('confort/', confort_view, name='confort'),    
   path('soins/', soins_view, name='soins'),
   path('histoire/', histoire_view, name='histoire'),
]
