from accounts.views import *
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
   path('inscription/',inscription, name='inscription') ,
   path('connexion/', LoginView.as_view(template_name='accounts/connexion.html'), name='connexion'),
   path('deconnexion/', LogoutView.as_view(next_page='home'), name='deconnexion'),
 
]
