# PROGETTO SCRAPER
Progetto scolastico ITIS mario delpozzo Cuneo, anno scolastico 2020

# PRESENTAZIONE PROGETTO
https://www.canva.com/design/DAD6txQBk1k/share/preview?token=h3KJIuJYpxPlZZQDQzeN0g&role=EDITOR&utm_content=DAD6txQBk1k&utm_campaign=designshare&utm_medium=link&utm_source=sharebutton

Bar down Char 

https://docs.google.com/spreadsheets/d/1DKGAYDYotlm0EIb-mK-M7uHJJuQeIsMDEHIXvoqa73s/edit?usp=sharing

# SUDDIVISIONE FEATURES E STORIES
Database: Protezione DB: Scelta tecnologica, Progettazione DB, Implementazione DB;

AlgoritmoScraping: Salvataggio su DB, Implementazione algoritmo, Automatizzazione algoritmo, Thredizzazione;

Interfaccia base: Home page, Dettaglio prodotto, Ricerca, Reindirizzamento, Presentazione elementi;

Interfaccia premium: Autocompletamento, Recenti, Popolari, Filtri, Guarda più tardi, Novità, Prezzi più bassi di sempre;

Login e registrazione: Tabella DB, Interfaccia accesso registrazione, Attivazione premium;

# SPIEGAZIONE STRUTTURA DATABASE TESTUALE e spezzone di codice 

Tabelle:

Utente(idUtente(pk), nome, cognome, email, password)

Prodotto(idProdotto(pk), categoria, marca, modello, descrizione, prezzo,nomeSito(fk))

Sito(nomeSito(pk), linkSito)

Utente:

idUtente(pk): int identificativo utente progressivo

nome: stringa(50) contiene il nome dell’utente

cognome: stringa(50) contiene il cognome dell’utente

email: stringa(75) contiene l’email dell’utente con il quale si è registrato per accedere ai privilegi offerti con la registarzione

password: stringa(30) contiene la password per accedere ai privilegi garantiti dalla registrazione, deve essere criptata per evitare che tutte le password siano visibili

Prodotto:

idProdotto(pk): numerico identificativo del prodotto

categoria: stringa(50) categoria al quale appartiene ilprodotto (tablet,telefoni...)

marca: stringa(50) marca del prodotto(Apple,Samsung...)

modello: stringa(50) modello del prodotto(Ps4,Ps5...)

descrizione: stringa(300) contiene la descrizione del prodotto

prezzo: float prezzo del prodotto

nomeSito(fk): stringa(50) nome del sito da cui proviene il prodotto

Sito:
nomeSito(pk): stringa(50) nome del sito

link: stringa(100) link del sito da cui proviene il prodotto

# COMUNICAZIONI DI LAVORO

    1. GIORDI : Ho aggiunto i due algoritmi di scraping dei siti unieuro e euronics, 
    ma sono proprio solo l’algoritmo quindi sono ancora da inserire completamente nel progetto e da integrare con django 
    
    2. GIOVA: aggiunto un altro file con il link alla presentazione che ho iniziato a impostare e 
    che dobbiamo condividere per sabato con Tosello, non l’ho fatta con power point perché Canva 
    è un bello strumento, gratis e facilissimo da usare per fare presentazioni professionali, 
    così rimane più bello, poi sto lavoro se riusciamo lo lasciamo agli altri che è facile.
    3. GIOVA: Ho aggiornato il progetto in modo che se vuoi vedere se sta salvando la roba da 
    qualche parte basta che al posto del salvataggio su json salvi su DB nella modalità come ti 
    lascio lo spezzone di codice qua sotto, poi se ti crei un progetto django e vai su l
    ocalhost:8000 ti fa vedere tutti prodotti salvati. 
    
    p = Products(prod_title = valoreNomeProdotto,
                prod_image = linkAllImmagine,
                prod_price = prezzoRilevato,
                prod_details = linkAlDettaglioDellaPagina
                prod_category = QualeCategoria)
    p.save()
    4. GIORDI: aggiunto altri due algoritmi di scraping (siti eprice e ollostore), a questo punto ne manca uno,
    proverò con amazon anche se il codice di html delle pagine di quel sito sono un’accozzaglia di tag senza classe.
    . vedrò che posso fare
    5. GIOVA: aggiunto il file iniziale del db progettato dall’analista Golè. Acconderò in seguito i miglioramenti 
    6. GIOVA: Ho anche messo tutto un po’ in ordine dividendo in cartelle, solo percè così non ci perdiamo nella baraonda
    7. GIOVA: creato i superutenti per la pagina admin, con questi  nome e pass poi ognun può cambiarsela appena entra
        7.1. mattia giordano123
        7.2. romeo gjokay123
        7.3. andrea golegole123
        7.4. hafez elsayed123
    8. GIOVA: Ho creato il database ho già anche caricato le categorie e i siti con le rispettive funzionalità, 
    ho poi creto una funzione che crea dinamicamente i link, nella funzione home, non è quello  il posto giusto 
    ma poi troveremo una posizione più consona
    9. GIORDI: Ho sistemato tutti gli algoritmi, ora prelevano i link dal db e salvano i dati sul db. Siamo a cavallo
    10. GIOVA: creato il tema della pagina home, a me sembra carino poi ditemi voi. Lo carico come separato e 
    poi lo integro nel progetto.
    11. GIORDI:sistemato le views dell'app compare_product, ho creato un fil scrapers.py per tutto 
    il codice di scraping. Inoltre ho threadizzato il processo di scraping, che richiede sempre parecchio tempo 
    (tipo 3 minuti buoni) ma così decisamente di meno.
    12. GIOVA: creato un template e sistemato quasi tutta la parte grafica, aspetto che gjock consegni 
    la sua parte e poi finiamo, che martedì ha anche detto che interroga.
    13. GIOVA: finito tutta la parte grafica, aspetto ancora che gjock faccia sto cazzo di form, 
    aspetto ancora un po’ poi lo faccio io, Comunque la grafica adesso è tutta a posto, ho messo anche una pagina di errore 404
