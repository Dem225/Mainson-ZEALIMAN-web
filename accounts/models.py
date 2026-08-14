from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Utilisateur(AbstractUser):
    telephone = models.CharField(max_length=20, blank=True)
    adresse = models.TextField(blank=True)
    ville = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return f"{self.adresse}-{self.telephone}-{self.ville}"


    
