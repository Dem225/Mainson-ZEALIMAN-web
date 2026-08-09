from django.db import models

# Create your models here.
# commandes/models.py
from django.db import models
from accounts.models import Utilisateur
from boutique.models import Produit

class Commande(models.Model):
    STATUTS = [
        ('en_attente', 'En attente'),
        ('validee', 'Validée'),
        ('expediee', 'Expédiée'),
        ('livree', 'Livrée'),
        ('annulee', 'Annulée'),
    ]
    client = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUTS, default='en_attente')
    adresse_livraison = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=0)

class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, related_name='lignes', on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
    quantite = models.PositiveIntegerField(default=1)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=0)