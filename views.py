from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import json

"""
AUTORE: Gruppo SCRUM
Data: sab 25 2020
Descrizione: scraper dei siti di prodotti di informatica
    schema generale: 
        -> funzione che si reca sulla pagina con tutte le categorie e raccoglie i link e li  
        salva in un file JSON con il nome della categoria per ogni link
        -> funzione che apre quel file e per ogni link raccolgie tutti i prodotti di quel sito
        
        
        ------ATTENZIONE-------
            le caratterisctiche raccolte sono in alcuni casi qualcuna in più o qualcuna in meno, 
            dovremo poi decidere con  precisione quali raccogliere
    

DA FARE: 
    - rendere lo scraper per amazon funzionante 
    - al posto che salvare su JSON salvare su DB
    - implementare stessa cosa anche per: (SONO PRESI COMPLETAMENTE A CASO SE NE CONOSCI DI MIGLIORI USA PUE QUELLI)
        https://www.monclick.it/vendite_pc-notebook-tablet 
        https://www.eprice.it/catalogo/informatica
    - controllare che da ogni sito i prodotti raccolti memorizzino le stesse cose
    
    - ..... aggiungi quello da aggiungere che ti viene in mente
"""

# E' tutto i funzioni perchè sto lavorando con django quindi funziona così, la parte importante è l'algoritmo
# all'interno

# pagina home
def home(request):
    return HttpResponse("Hello, world. I'm the home.")

# funzione che raccoglie i link alle pagine del sito euronics
def euronics_link(request):

    #voglio ricevere tutti i link dalla pagina con le categorie
    BASE_URL = 'https://www.euronics.it/computer-tablet/cat90046/'

    #richiesta get al BASE_URL, pagina con tutte le categorie
    res = requests.get(BASE_URL)
    # prendo il testo della riposta
    data = res.text

    #istanzio un oggetto Soup e lo uso per parsificare il text
    soup = BeautifulSoup(data, features='html.parser')

    #cerco tutti gli elementi nella lista con classe specificata, ovvero tutte le categorie
    link_listing = soup.find_all('li', {'class':'navBrand__item'})

    #creo lista con link alle categorie
    links = []

    #per ogni sezione html trovata estraggo url alla categoria e nome della categoria
    for link in link_listing:
        #estraggo url e categoria
        link_url = link.find('a').get('href')
        link_type = link.find(class_='navCategory__category').text
        #inserisco entrambe in una lista
        links.append((link_url, link_type))

    # scrivo su un file JSON ---> dovrà diventare scrittura su DB
    filename = 'linksEuronics.json'
    #apro il file in modalità scrittura
    fw = open(filename, 'w')
    #scrivo sul file, la funzione dumps trasforma una lista in oggetto JSON
    fw.write(json.dumps(links))
    fw.close()

    #restituisco una risposta http solo per comunicare all'utente online che è andato tutto bene
    return HttpResponse("Scraping your links.....")

# funzione che raccoglie e salva tutti i prodotti
def scrape_cards_euronics(request):

    #apro il JSON scritto dalla funzione euronics_link
    filename = 'linksEuronics.json'
    #apro in modalità lettura
    fw = open(filename, 'r')
    #leggo tutto
    links = fw.read()
    #chiudo il file
    fw.close()
    #trasformo il json in una lista con la funzione load
    link_list = json.loads(links)

    #creo una lista vuota a cui appenderò i risultati
    cards = []
    #per ogni link
    for i in range(len(link_list)):

        # racccolgo l'url che avevo salvato e richiedo la pagina
        url = link_list[i][0]
        # effettua la richiesta
        res = requests.get(url)

        #istanzia oggetto soup
        soup = BeautifulSoup(res.text, 'html.parser')

        #cerco la lista dei prodotti ottenuti
        listing = soup.find_all('div', {'class':'productCard'})

        #per ogni prodotto ottenuto
        for product in listing:
            #ricavo nome, casa costruttrice, categoria, immagine, prezzo

            # TO DO aggiungere pagina di dettaglio

            #inserire controllo..
            prod_name = product.find(class_='productCard__name').text
            prod_brand = product.find(class_='productCard__brand').text
            prod_category = product.find(class_='productCard__category').text
            prod_image = product.find(class_='productCard__image').get('src')
            try:
                prod_price = product.find(class_='productCard__price').text
            except:
                prod_price = None

            #appendo quanto ottenuto come un'elemento alla lista "cards"
            cards.append([prod_name, prod_brand, prod_category, prod_image, prod_price])

    #salvo i risultati su un file JSON
    filename = 'products.json'
    # apro file
    fw = open(filename, 'w')
    #scrivo tutta la lista parsificata in JSON grazie al metodo dumps
    fw.write(json.dumps(cards))
    #chiudo il file
    fw.close()

    return HttpResponse("I'm working on euronics.....")

"""
Lo scraper sul sito della trony sostanzialmente lavora allo stesso moodo di quello su euronics
"""
def trony_links(request):
    # voglio ricevere tutti i link dalla pagina delle categorie
    BASE_URL = 'https://www.trony.it/online/informatica_ct-VHJvbnktQjJDLVRyb255fHx8MTc'

    # richiesta get al BASE_URL, pagina con tutte le categorie
    res = requests.get(BASE_URL)
    # prendo il testo della riposta
    data = res.text

    # istanzio un oggetto Soup e lo uso per parsificare il text
    soup = BeautifulSoup(data, features='html.parser')

    # cerco tutti gli elementi nella lista con classe specificata
    link_listing = soup.find_all('div', {'class': 'subcategory_list_box_container'})

    # creo lista con link alle categorie
    links = []
    for link in link_listing:
        # estraggo url e categoria
        link_url = link.find('a').get('href')
        link_type = link.find_all(class_='subcategory_list_box_text')[1].text
        links.append((link_url, link_type))

    filename = 'linksTrony.json'
    fw = open(filename, 'w')
    fw.write(json.dumps(links))
    fw.close()

    return HttpResponse("Scraping your TRONY links.....")

def scrape_cards_trony(request):

    #legge dal JSON e cercare tutti i valori nei vari siti

    filename = 'linksTrony.json'
    fw = open(filename, 'r')
    jsonText = fw.read()
    fw.close()
    links = json.loads(jsonText)

    cards = []
    for i in range(len(links)):
        #per ogni categoria appendo il mio nuovo elemento alla lista, poi scrivo tutto
        url = links[i][0]
        res = requests.get(url)

        soup = BeautifulSoup(res.text, 'html.parser')

        # cerco la lista dei prodotti ottenuti
        listing = soup.find_all('div', {'class':  'smcc-listing-risultati-prodotto'})

        #per ogni prodotto ottenuto
        for product in listing:
            #ricavo nome,  categoria, link al prodotto sul  sito( così potremo reindirizzare), immagine, prezzo
            prod_name = product.find(class_='listing_risultati_prodotto_2').text
            prod_category = product.find(class_='listing_risultati_prodotto_1').text
            prod_details = product.find(class_='product-photo').find('a').get('href')
            prod_image = product.find('div', {'class':'product-photo'}).find('img').get('data-src')
            try:
                prod_price = product.find(class_='ish-priceContainer').text
            except:
                prod_price = None

            cards.append([prod_name, prod_category, prod_image, prod_price, prod_details    ])

    filename = 'productsTrony.json'
    fw = open(filename, 'w')
    fw.write(json.dumps(cards))
    fw.close()

    return HttpResponse("I'm working.....")

"""
------ ATTENZIONE --------
Questo sito non avendo una pagina da cui trovare i  link alle varie paagin devo aggiustarmi in modo diverso

Quindi leggo uno dei due file dei links e estraggo il nome della categoria
A qeusto punto costruisco degli  url  in modo che sembri che io ho scritto il nome della categoria nella barra 
di ricerca del sito, poi a questo punto scarico il risultato ottenuto

Nelle pagina di raccolta dei prodotti non cambia nulla di nuovo, cambia qualcosa in quella di creazione dei link
"""
def amazon_links(request):

    #url base, quello che compare quando scrivo qualcosa nella barra ricercche
    base_url = 'https://www.amazon.it/computer/s?k={}'

    #apro il file della trony con i link e ricavo le categorie
    fw = open('links.json', 'r')
    jsonText = fw.read()
    fw.close()
    #ho una lista con link e categoria
    categories = json.loads(jsonText)

    #voglio creare una lista di link per amazon
    links= []
    for i in range(len(categories)):
        #concateno all' url di base la categoria in modo da avere un link, anche se in acluni
        # casi ci sono degli spazi, il dispatcher amazon sa gestirli
        cat = categories[i][1]
        links.append((base_url.format(cat), cat))


    #scrivo risultati su fle json
    filename = 'linksAmazon.json'
    fw = open(filename, 'w')
    fw.write(json.dumps(links))
    fw.close()

    return HttpResponse("Scraping your AMAZON links.....")

#lo scheletro di questa funzione è uguale a tutte le altre, non funziona ancora però
def scrape_cards_amazon(request):

    filename = 'linksAmazon.json'
    fw = open(filename, 'r')
    jsonText = fw.read()
    fw.close()
    links = json.loads(jsonText)

    cards = []
    for i in range(2):#len(links)
        #per ogni categoria appendo il mio nuovo elemento alla lista, poi scrivo tutto
        url = links[i][0]
        res = requests.get(url)
        print('scraping on ' + url)
        soup = BeautifulSoup(res.text, 'html.parser')

        # cerco la lista dei prodotti ottenuti
        listing = soup.find_all('div', {'class': 's-include-content-margin s-border-bottom s-latency-cf-section'})
        print('printing all the items founded %d ' %len(listing))
        #per ogni prodotto ottenuto
        for product in listing:
            #ricavo nome, casa costruttrice, categoria, immagine, prezzo
            #inserire controllo..
            prod_name = product.find(class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2').text
            #product.find(class_='title').find('a').get('href')
            #prod_brand = product.find(class_='category').text non è presente in unieuro
            prod_details = product.find(class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2').find('a').get('href')
            prod_image = product.find(class_='a-section aok-relative s-image-fixed-height').find('img').get('src')

            try:
                prod_price = product.find(class_='a-price-whole').text
            except:
                prod_price = None

            cards.append([prod_name, prod_image, prod_price, prod_details])

    #filename = 'productsAmazon.json'
    #fw = open(filename, 'w')
    #fw.write(json.dumps(cards))
    #fw.close()

    return HttpResponse("I'm working.....")


