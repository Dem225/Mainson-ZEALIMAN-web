from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Utilisateur

class InscriptionForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'telephone', 'adresse', 'ville', 'password1', 'password2']



