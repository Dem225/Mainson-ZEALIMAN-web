from boutique.panier import Panier

def panier_context(request):
    panier = Panier(request)
    return {
        'panier_count': len(panier)
    }