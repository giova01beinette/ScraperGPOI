from django.http import HttpResponse
from .models import Siti, Categorie, Links, Prodotti

from . import scrapers

# costruisce tutti i link unendo siti e categorie, va richiamata solo se si sono apportate modifiche alla tabella siti e/o categorie
# dopo essere stata richiamata, inserire manualmente nella tabella Links le pagine da visitare dove necessario (Euronics/desktop = 3)
def make_links(request):
    # ricevere il database con tutti i siti e ricevere quello con tutte le categorie
    # lopppare per ogni sito e poi per ogni categoria creare il nuovo link con riferimento alla categoria e al sito
    Links.objects.all().delete()
    siti = Siti.objects.all()
    categorie = Categorie.objects.all()
    for sito in siti:
        for categoria in categorie:
            stringLink = (sito.sito_link_base + categoria.categoria_nome)
            newRecord = Links(link= stringLink,
                         categoria=categoria,
                         sito=sito)
            newRecord.save()

    return HttpResponse("ho creato tutti i link .... o almeno ci ho provato")

# funzione che quando richiamata esegue lo scraping su tutti i siti, svuola la tabella prodotti e poi la riempe con i nuovi dati
def collect(request):
    scrapers.scrape()
    return HttpResponse("All scraped everywere and db updated!")