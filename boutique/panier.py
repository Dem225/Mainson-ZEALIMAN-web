# boutique/panier.py
from boutique.models import Produit

class Panier:
    def __init__(self, request):
        self.session = request.session
        panier = self.session.get('panier')
        if panier is None:
            panier = self.session['panier'] = {}
        self.panier = panier

    def ajouter(self, produit, quantite=1):
        produit_id = str(produit.id)
        if produit_id in self.panier:
            self.panier[produit_id]['quantite'] +=quantite
        else:
            self.panier[produit_id] = {
                    'quantite': quantite,
                    'prix': str(produit.prix)
                }
        self.session.modified = True

    def __iter__(self):
        for produit_id, infos in self.panier.items():
            produit = Produit.objects.get(id=produit_id)
            yield {
                'produit': produit,
                'quantite': infos['quantite'],
                'prix': infos['prix'],
                'total_prix': float(infos['prix'] ) *  infos['quantite']
            }
        pass
    def __len__(self):
      
     return sum(infos['quantite'] for infos in self.panier.values())

    def get_total(self):
        return  sum( float(infos['prix']) * infos['quantite'] for infos in self.panier.values())
