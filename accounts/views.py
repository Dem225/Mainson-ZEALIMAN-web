from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.forms import InscriptionForm
from accounts.models import Utilisateur

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'inscription a été bien exécutée")
            return redirect('connexion')
        else:
            messages.error(request, "Merci de corriger les erreurs du formulaire")
    else:
        form = InscriptionForm()

    context = {'form': form}
    return render(request, 'accounts/inscription.html', context)
