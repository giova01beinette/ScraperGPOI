# importo due packages che mi serviranno per parsificare l'html (bs4->BeautifulSoup)
# e per interrogare un server (request -> urlopen)
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

#ciclo for per visitare le prime tre pagine del sito (12x3=36 prodotti)
for n in range(1, 4):
    # url della pagina che intendo visitare
    my_url = 'https://www.euronics.it/desktop/cat110202/?p=' + str(n)

    # creo un client che apre la connessione 
    # e scarica il contentuto della pagina
    client = urlopen(my_url)
    page_html = client.read()
    client.close()

    # parsificazione dell'html
    page_soup = soup(page_html, "html.parser")

    # prelevo il contenuto di tutti i tag div di classe /vedi sotto/ in cui sono contenute tutte le 
    # informazioni del prodotto che ci interessano
    cards = page_soup.findAll("div",{"class":"productCard j-productCard j-comparisonItem"})

    #apro il file json in scrittura
    filename = "result.json"
    fw = open(filename, "a")

    # ciclo for che scorre tutti gli elementi
    for card in cards:
        # recupero il div che ha tutte le informazioni del prodotto tranne il prezzo
        card_text=card.find("div",{"class":"productCard__text"})
        brand = card_text.find("span",{"class":"productCard__brand"}).text
        nome = card_text.find("h2",{"class":"productCard__name"}).text
        # recupero il div che contiene il prezzo
        card_price=card.find("div",{"class":"productCard__priceWrapper"}) 
        #alcuni prodotti non hanno il prezzo, utilizzo una try
        try:
            prezzo = card_price.find("span",{"class":"productCard__price"}).text.strip() #strip() rimuove tutto ciò che non è testo (es \n\r)
        except:
            prezzo = None
        
        #stampo i valori
        print("brand: " + brand)
        fw.write("{\"brand\":\""+brand+"\" , ")  
        print("nome: " + nome)
        fw.write("\"nome\":\""+nome+"\" , ")
        if prezzo is not None:
            print("prezzo : " + prezzo)
            fw.write("\"prezzo\":\""+prezzo+"\"}\n")
        else:
            print("prezzo : non disponibile")
            fw.write("\"prezzo\":\"non disponibile\"}\n")
    
    fw.close()

    


