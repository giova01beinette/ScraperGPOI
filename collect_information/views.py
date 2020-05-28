# importo due packages che mi serviranno per parsificare l'html (bs4->BeautifulSoup)
# e per interrogare un server (request -> urlopen)
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import json
from django.http import HttpResponse
# importo webdriver da selenium, per saperne di più -> https://riptutorial.com/it/selenium-webdriver/example/5257/cos-e-selenium-webdriver-
# importo time per utilizzare il comndo sleep
# importo json per serializzare in formato json
from selenium import webdriver
import time
from .models import Siti, Categorie, Links, Prodotti
from django.shortcuts import render

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

def empty_table_prodotti(request):
    # funzione che svuota la tabella Prodotti, va richiamata ogni volta prima di fare lo scraping
    Prodotti.objects.all().delete()
    return HttpResponse("ho svuotato la tabella prodotti")

def scrape_euronics(request):
    # ricavo dalla tabella Links tutti i record riguardanti il sito interessato
    lista_link = Links.objects.filter(sito = Siti.objects.get(sito_nome='euronics')) 
    
    # ciclo per ogni categoria
    for i in range(0, len(lista_link)):
        link = lista_link[i].link
        num_pagine = lista_link[i].numero_pagine
        # ciclo per il numero di pagine indicate nella lista
        for n in range(1, (num_pagine + 1)):
            # aggiungo il parametro del numero della pagina all'url
            my_url = link + '&p=' + str(n)

            # creo un client che apre la connessione
            # e scarica il contentuto della pagina
            client = urlopen(my_url)
            page_html = client.read()
            client.close()

            # parsificazione dell'html
            page_soup = soup(page_html, "html.parser")

            # prelevo il contenuto di tutti i tag div di classe /vedi sotto/ in cui sono contenute tutte le
            # informazioni del prodotto che ci interessano
            cards = page_soup.findAll("div", {"class": "productCard j-productCard j-comparisonItem"})

            # ciclo for che scorre tutti gli elementi
            for card in cards:
                # recupero il div che contiene brand e nome
                card_text = card.find("div", {"class": "productCard__text"})
                brand = card_text.find("span", {"class": "productCard__brand"}).text
                nome = card_text.find("h2", {"class": "productCard__name"}).text
                # recupero il div che contiene il prezzo
                card_price = card.find("div", {"class": "productCard__priceWrapper"})
                # alcuni prodotti non hanno il prezzo, utilizzo una try
                try:
                    prezzo = card_price.find("span", {
                        "class": "productCard__price"}).text.strip()  # strip() rimuove tutto ciò che non è testo (es \n\r)
                except:
                    prezzo = None
                # recupero il div che contiene l'immagine
                image_wrapper = card.find("div", {"class": "productCard__imageWrapper"})
                immagine = image_wrapper.find("img")['src']
                # recupero il link nel primo tag <a> con attributo href
                link_prod = card.find("a", href=True)['href']

                if prezzo is None:
                    prezzo = "non disponibile"
                # salvo i valori sul database
                newRecord = Prodotti(nome = nome,
                                     brand = brand,
                                     prezzo = prezzo,
                                     link_immagine = immagine,
                                     link_dettaglio = link_prod,
                                     link = lista_link[i])
                newRecord.save()

    return HttpResponse("All scraped on euronics")

def scrape_ollostore(request):
    # ricavo dalla tabella Links tutti i record riguardanti il sito interessato
    lista_link = Links.objects.filter(sito = Siti.objects.get(sito_nome='ollostore'))

    # ciclo per ogni categoria
    for i in range(0, len(lista_link)):
        link = lista_link[i].link
        # ciclo per otto pagine per categoria in modo da ottenere circa 100 prodotti per ognuna
        for n in range(1, 9):
            # aggiungo il parametro del numero della pagina all'url
            my_url = link + "&page=" + str(n)

            # creo un client che apre la connessione
            # e scarica il contentuto della pagina
            client = urlopen(my_url)
            page_html = client.read()
            client.close()

            # parsificazione dell'html
            page_soup = soup(page_html, "html.parser")

            # prelevo il contenuto di tutti i tag div di classe /vedi sotto/ in cui sono contenute tutte le
            # informazioni del prodotto che mi interessano
            containers = page_soup.findAll("div", {
                "class": "box_product relative"})  # potresti dover aggiungere uno spazio alla fine della classe (dipende dallo user-agent)

            # ciclo for che scorre tutti gli elementi
            for container in containers:
                # recupero brand, nome, prezzo, immagine e link
                nome = container.find("div", {"class": "product-name"}).h2.a.text
                # il brand è sempre la prima parola del nome
                brand = str(nome).split(' ', 1)[0]
                prezzo = container.find("span", {"class": "itemPrice redB1 main-product-price"}).text
                immagine = container.find("span", {"class": "product-image-box"}).img['src']
                link_prod = container.find("a", href=True)['href']

                 # salvo i valori sul database
                newRecord = Prodotti(nome = nome,
                                     brand = brand,
                                     prezzo = prezzo,
                                     link_immagine = immagine,
                                     link_dettaglio = 'https://www.ollo.it' + link_prod,
                                     link = lista_link[i])
                newRecord.save()
            
    return HttpResponse("All scraped on ollostore")

def scrape_eprice(request):
    # ricavo dalla tabella Links tutti i record riguardanti il sito interessato
    lista_link = Links.objects.filter(sito = Siti.objects.get(sito_nome='eprice'))

    # avvio il driver indicando nell'executable_path il percorso sul mio pc del web engine di firefox "geckodriver", scaricabile da https://github.com/mozilla/geckodriver/releases
    driver = webdriver.Firefox(executable_path= '.\\geckodriver')

    # ciclo per ogni categoria
    for i in range(0, len(lista_link)):
        link = lista_link[i].link
        # ciclo per le prime tre pagine in modo da ottenere 108 risultati per categoria (circa 100)
        for n in range(1, 4):
            # aggiungo il parametro del numero della pagina all'url
            my_url = link + "&page=" + str(n)
            # ottengo la pagina web
            driver.get(my_url)
            # eseguo uno script che scorre la pagina fino al basso
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            # aggiungo uno sleep time di 10 secondi per aspettare che la pagina sia completamente caricata
            time.sleep(10)
            # a questo punto ricerco gli elementi che mi interessano tramite il loro xpath, che serve per raggiungere un determinato nodo in xml
            containers = driver.find_elements_by_xpath("//*[@id='root']/main/div/section//a[@class='ep_prodListing']")

            # ciclo per ogniu prodotto
            for container in containers:
                # recupero brand, nome, prezzo, immagine e link
                nome = container.find_element_by_class_name('ep_prodContTxt').find_element_by_tag_name('p').text
                # il brand è sempre la prima parola del nome
                brand = brand = str(nome).split(' ', 1)[0]
                prezzo = container.find_element_by_class_name('ep_contPrice').find_element_by_tag_name('span').text
                immagine = container.find_element_by_class_name('ep_prodImg').find_element_by_tag_name(
                    'img').get_attribute("src")
                link_prod = container.get_attribute("href")

                # salvo i valori sul database
                newRecord = Prodotti(nome = nome,
                                     brand = brand,
                                     prezzo = prezzo,
                                     link_immagine = immagine,
                                     link_dettaglio = link_prod,
                                     link = lista_link[i])
                newRecord.save()

    # chiusura del driver
    driver.quit()

    return HttpResponse("all scraped on eprice")


def scrape_unieuro(request):
    # ricavo dalla tabella Links tutti i record riguardanti il sito interessato
    lista_link = Links.objects.filter(sito = Siti.objects.get(sito_nome='unieuro'))

    # avvio il driver indicando nell'executable_path il percorso sul mio pc del web engine di firefox "geckodriver", scaricabile da https://github.com/mozilla/geckodriver/releases
    driver = webdriver.Firefox(executable_path='.\\geckodriver')
                                               
    # ciclo per ogni categoria
    for i in range(0, len(lista_link)):
        link = lista_link[i].link
        # ciclo per le prime tre pagine in modo da ottenere 96 risultati per categoria (circa 100)
        for n in range(0, 3):
            # aggiungo il parametro della pagina all'url
            my_url = link + "&p=" + str(n)

            # ottengo la pagina web
            driver.get(my_url)
            # eseguo uno script che scorre la pagina fino al basso
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            # aggiungo uno sleep time di 10 secondi per aspettare che la pagina sia completamente caricata
            time.sleep(10)

            # a questo punto ricerco gli elementi che mi interessano tramite il loro xpath, che serve per raggiungere un determinato nodo in xml
            # (lo si può ottenere tramite lo strumento ispeziona del brower)
            results = driver.find_elements_by_xpath(
                "//*[@id='instant-results']/div[1]/main/div[3]/section//section/article/div/div[1]")
            # DEBUG->print('Firefox Webdriver - Number of results', len(results))

            # ciclo per ogni tag <div class="info">, dove sono contenute tutte le informazioni che mi interessano
            for result in results:
                # trovo il tag <div class="title"> che contiene nome e link del prodotto
                title = result.find_element_by_class_name('title')
                nome = title.find_element_by_tag_name('a').text
                link_prod = title.find_element_by_tag_name('a').get_attribute("href")
                # questo sito non registra il brand del prodotto, che è la prima parola del nome del prodotto stesso (rare eccezioni)
                brand = str(nome).split(' ', 1)[0]
                # trovo il tag <div class="product-img-container"> e al suo interno il tag a che contiene l'immagine
                img_container = result.find_element_by_class_name('product-img-container').find_element_by_tag_name('a')
                immagine = img_container.find_element_by_tag_name('img').get_attribute("data-src")
                # trovo il tag <div class="price"> che contiene il prezzo del prodotto
                prezzo = result.find_element_by_class_name('price').text

                # salvo i valori sul database
                newRecord = Prodotti(nome = nome,
                                     brand = brand,
                                     prezzo = prezzo,
                                     link_immagine = immagine,
                                     link_dettaglio = link_prod,
                                     link = lista_link[i])
                newRecord.save()

    # chiusura del driver
    driver.quit()
    return HttpResponse("all scraped on unieuro")

"""def trony_links(request):
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

    return HttpResponse("I'm working.....")"""
