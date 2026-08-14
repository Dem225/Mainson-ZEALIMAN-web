from django.contrib import admin
from boutique.models import Categorie, Produit

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'prix', 'stock', 'disponible')
    list_filter = ('disponible', 'categorie')
    search_fields = ('nom',)
    prepopulated_fields = {'slug': ('nom',)}

admin.site.register(Categorie)