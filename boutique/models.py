from django.db import models

# Create your models here.
# boutique/models.py

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    def __str__(self):
            return f"{self.nom}-{self.slug}"

class Produit(models.Model):
    nom = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=0)  # FCFA, pas de centimes
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='produits/')
    stock = models.PositiveIntegerField(default=0)
    disponible = models.BooleanField(default=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom}-{self.slug}-{self.disponible}-{self.date_ajout}"