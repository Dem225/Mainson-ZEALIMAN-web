from django.contrib import admin
from commandes.models import Commande
from commandes.models import LigneCommande
# Register your models here.

admin.site.register(Commande)
admin.site.register(LigneCommande)
