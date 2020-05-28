from django.shortcuts import render
from collect_information.models import Prodotti, Categorie, Links

# Create your views here.
def home(request):
    return render(request, 'compareProductOnline/index.html')

def category(request):

    # devo fare in modo che venga chimata questa schermata passsando un "paramentro" diverso,
    # lo prendo estraggo quacosa per quella
    # categoria e lo mostro
    categoria = request.GET.get('category')
    ricerca = request.GET.get('product')
    new = request.GET.get('new')

    titleFrontend = ""
    resultForFrontend = []

    if categoria != None:

        cat = Categorie.objects.filter(categoria_nome=categoria.lower().replace(" ", "%20")).first()
        links = cat.links_set.all()
        for l in links:
            prods = Prodotti.objects.filter(link=l)[:10]
            for prod in prods:
                resultForFrontend.append(prod)
        titleFrontend = categoria

    # se è stato passato un valore di ricerca
    if ricerca != None:
        prodotti = Prodotti.objects.filter(nome__contains=ricerca)
        if len(prodotti) == 0:
            ricerca = None
        titleFrontend = ricerca
        resultForFrontend = prodotti

    if new != None :
        #se viene chiamata dalla barra di navigazione non ha senso dare errore è ovvio che si verifichi
        #mostrosemplicemnte 10 prodotti e passo nel titolo immetti la ricerca
        resultForFrontend = Prodotti.objects.all()[:15]
        titleFrontend = "Anteprima dei prodotti"

    data_to_frontend = {
        'search': titleFrontend,
        'products': resultForFrontend,
    }
    if ricerca == None and categoria == None and new == None:
        return render(request, 'compareProductOnline/404.html')

    return render(request, 'compareProductOnline/search.html', data_to_frontend)
