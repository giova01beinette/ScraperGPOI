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

    if categoria == None:
        return render(request, 'compareProductOnline/404.html')

    cat = Categorie.objects.filter(categoria_nome=categoria.lower().replace(" ","%20")).first()
    print(cat)
    links = cat.links_set.all()
    result = []
    for l in links:
        prods = Prodotti.objects.filter(link=l)[:10]
        for prod in prods:
            result.append(prod)


    stuff_to_frontend = {
        'search': categoria,
        'products': result,
    }
    return render(request, 'compareProductOnline/search.html', stuff_to_frontend)
