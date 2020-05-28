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

# COMPATECH

OBIETTIVO

L’obiettivo principale era lo sviluppo di un componente per il reperimento di informazioni nel web. Le informazioni da ricercare sono relative ad hardware elettronici di diversi siti di e-commerce, quali Euronics, ePrice, OlloStore, Unieuro.

L’IDEA

L’idea della proposta del progetto nasce dall’esigenza di raccogliere i prodotti presenti
su Internet da una serie di siti di e-commerce, visualizzati all’interno della piattaforma Compatech
dai clienti. Le categorie di prodotti da ricercare sono: Desktop, Notebook, Smartphone e Hard Disk. L’inizio della ricerca avviene fornendo il nome del prodotto desiderato oppure selezionando una delle 4 categorie disponibili per dare un’occhiata generale. L’azienda richiede lo sviluppo di un web scraper per automatizzare il processo di reperimento e inserimento dei dati all’interno della
piattaforma Compatech.


ASPETTATIVE

Lo sviluppo dello scraper permette al sito Compatech di garantire una funzionalità molto importante. Questo componente, infatti, migliora l’esperienza utente all’interno della piattaforma e presenta il vantaggio di automatizzare il processo di zapping tra un sito e un altro alla ricerca del
prezzo più basso, perché la ricerca non è più a carico dell’utente ma bensì viene svolta dal sistema. Questo riduce il tempo necessario all’intermediario per reperire le informazioni manualmente al di fuori della piattaforma.


TIPOLOGIA DI CLIENTELA

La piattaforma è indirizzata a chiunque voglia effettuare un acquisto online e desideri avere un rapido riscontro tra le opportunità che offrono i diversi siti di e-commerce sul web.


TECNOLOGIE UTILIZZATE 

Il sistema è composto da:
• Front end: è la parte visibile dagli utenti e con la quale essi interagiscono.
Nella piattaforma Compatech, il front end è una web app che permette ai clienti di ricercare prodotti e, per ognuna di queste, mostrarne il sito di provenienza e il relativo prezzo.
• Back end: è la parte non visibile dagli utenti. Il back end si occupa di raccogliere i dati tramite l’algoritmo proprietario, andandoli a prelevare dai diversi siti, salvandoli su un database.

Il codice riguardante il back end è sviluppato in linguaggio Python e gestito dal web framework Django. Il front end è sviluppato in linguaggio JavaScript, facendo uso del framework Bootstrap. Un framework è un’architettura logica di supporto su cui un software può essere progettato e realizzato, spesso facilitandone lo sviluppo da parte del programmatore.


ANALISI DEI RISCHI

Durante la fase iniziale sono stati individuati alcuni possibili rischi che si sarebbero potuti verificare. 

-Difficoltà tecnologica: conoscenza base del linguaggio Python e non conoscenza delle
tecnologie da utilizzare. Consultare la documentazione delle rispettive tecnologie o altre
fonti presenti sul web.
 
-Difficoltà di realizzazione: i servizi di terze parti potrebbero non offrire il servizio richiesto oppure le funzionalità richieste sono troppo complesse. In caso si verifichi il rischio, verrà analizzato il problema per trovare una soluzione.
 
-Rischio di non finire in tempo: lo sviluppo del progetto potrebbe non terminare entro la data prestabilita. Una soluzione preventiva è pianificare le attività con margine e ottimizzare il tempo a
disposizione. 



TECNOLOGIE E STRUMENTI

In questa sezione vengono descritte le tecnologie, gli strumenti e le librerie utilizzate
durante lo sviluppo del progetto. Per ognuno di essi viene descritto il motivo della scelta e
dove viene utilizzato all’interno del progetto.


PYTHON

Python è un linguaggio pseudo-compilato, ciò significa che è presente un interprete,
che si occupa di analizzare il codice sorgente e, se sintatticamente corretto, di eseguirlo.
Python presenta numerose caratteristiche, tra cui le seguenti:
• è un linguaggio ad alto livello molto semplice, potente e molto performante
rispetto ad altri linguaggi interpretati;
• è multi-paradigma, cioè supporta sia la programmazione procedurale, sia la
programmazione ad oggetti, includendo funzionalità come l’ereditarietà singola,
l’ereditarietà multipla e l’overloading degli operatori;
• è portabile, infatti lo stesso programma può funzionare su piattaforma Linux,
Mac o Windows purché vi sia installato un interprete compatibile;
• è fornito di un’estesa libreria standard, ma è possibile installare numerose altre
librerie create e mantenute dalla comunità.
Un grande vantaggio di Python rispetto a altri linguaggi di progrmamazione più ostici, è la possibilità di usare IDLE, una shell interattiva che esegue le istruzioni in tempo reale (senza dover stare a compilare / lanciare di volta in volta uno script, come succede per altri linguaggi compilati).
Ho utilizzato Python versione 3 per lo sviluppo dell’intero progetto. La scelta è ricaduta su Python anche per la sua incline predisposizione ad effettuare agoritmi di scraping, grazie ad esempio alla sua libreria Beautiful Soup. Inoltre, la possibilità di scoprire un nuovo linguaggio di programmazione così semplice e completo, considerato tra i migliori per lavori di questo tipo, non poteva lasciarci indifferenti. 


DJANGO


Django è un web framework, scritto in Pyhton, per lo sviluppo di applicazioni web
seguendo il paradigma “Model-Template-View”. Il progetto è sviluppato dalla “Django
Software Foundation”, è gratuito ed open source. Django fornisce un certo
numero di funzionalità che facilitano il rapido sviluppo di applicazioni per la gestione
di contenuti web, tra cui:
• Astrazione del database e robusta API (Application Programming Interface) per
gestirlo. Con API si intende un insieme di metodi di comunicazione chiaramente
definiti tra componenti;
• Possibilità di installare funzionalità tramite plugin, cioè programmi non autonomi
che interagiscono con un altro programma per estenderne le funzioni;
• Fornisce un’interfaccia amministrativa che permette di creare, aggiornare ed
eliminare contenuti rappresentati da oggetti, tenendo traccia delle operazioni
effettuate;
• Gestore di URL (Uniform Resource Locator) basate su espressioni regolari;
• Supporto per la localizzazione, incluse traduzioni dell’interfaccia amministrativa;
• Sistema di gestione degli utenti e della loro autenticazione nell’applicazione web.
Il web scraper è stato integrato in Django e il suo utilizzo è stato spontaneo, in quanto al suo interno include già una quantità enorme di strumenti pronti all’uso. In questo modo quando hai in mente un’idea per un’applicazione, non dovrai preoccuparti di molte cose in quanto Django se ne prenderà cura al tuo posto. Inoltre Django, al suo interno, include già tutte le funzionalità per la creazione di form, dell’impaginazione, della verificare che i dati inseriti dall’utente siano corretti, che i campi obbligatori siano stati inseriti, lasciando a noi solo la logica che sta dietro.


SQLITE

SQLite è una libreria software scritta in linguaggio C che implementa un DBMS SQL di tipo ACID incorporabile all'interno di applicazioni. Un DBMS è un sistema software progettato per consentire la creazione, la manipolazione e l’interrogazione efficiente di database. Questo software è incluso in Python, perciò non c’è bisogno di installare nient’altro come supporto per il database.
In SQLite vengono salvati tutti i dati dell’architettura esistente.


PYCHARM

PyCharm è un ambiente di sviluppo integrato (IDE), sviluppato da JetBrains c , usato
nella programmazione in linguaggio Python. Fornisce l’analisi del codice, un debugger
grafico, un tester integrato, l’integrazione con i sistemi di controllo versione e supporta
lo sviluppo web con Django.14. Questo strumento è stato scelto per la potenza che offre, infatti con PyCharm è possibile gestire il controllo di versione e la macchina virtuale; inoltre, rispetto ad altri IDE, permette un’analisi del codice più avanzata.


GITHUB

GitHub è un servizio web di hosting per progetti software che usa il software di controllo
di versione distribuito Git. Principalmente utilizzato dagli sviluppatori, che caricano il
codice sorgente dei loro programmi per renderlo disponibile agli utenti. Quest’ultimi
possono interagire con lo sviluppatore tramite pull request, commenti e un sistema di
issue tracking per migliorare il codice, risolvendo bug, o aggiungendo funzionalità al
prodotto.

# LIBRERIE


REQUESTS

Requests è una libreria Python semplice ed elegante che consente l’invio di richieste
HTTP/1.1 in modo automatico, evitando allo sviluppatore l’aggiunta dei parametri
per configurare e gestire la connessione.
Abbiamo scelto di utilizzare questa libreria per effettuare le richieste alle API utilizzate nello
sviluppo dei due componenti, perché permette di gestire richieste HTTP in modo semplice e con un corretto livello di astrazione.


BEAUTIFUL SOUP

Beautiful Soup è una libreria Python per estrarre dati da file HTML e XML. Essa
crea un albero di analisi per le pagine analizzate, il che è particolarmente utile per il
web scraping.
Beautiful Soup è stata utilizzata per la realizzazione del web scraper, analizzando il codice sorgente delle pagine web. Questa libreria è stata scelta per due vantaggi importanti: permette di scegliere il parser di analisi ed è in grado di analizzare anche linguaggio di markup non valido, ad esempio
tag non chiusi.


SELENIUM

Selenium è una suite di strumenti, scritti in Java, per l’automazione di un browser
web su diverse piattaforme. Nello specifico, abbiamo utilizzato Selenium Webdriver che
accetta comandi e li invia al browser tramite driver specifici.
Abbiamo scelto scelto questa libreria perché è open source e supporta diversi browser.


PROGETTAZIONE E SVILUPPO

Il progetto si articola in due componenti: il componente di scraping e il componente compareProduct. Lo scraper si occupa della ricerca sul web di informazioni relative ai prodotti. 
Il componente compareProduct consente di ricavare dal database i prodotti ottenuti grazie allo scraping. 


SCRAPER

Il principale obiettivo del progetto è stato lo sviluppo di un componente di web scraping che si occupa di:
1. Ricercare i prodotti facenti parti le categorie Notebook, Desktop, Smartphone e hard Disk da siti che abbiamo selezionato
2. Ottenere le principali informazioni (nome, brand, prezzo, immagine...) del prodotto
3. Salvare le informazioni sul database.

 
COMPARE PRODUCT

All’interno della piattaforma, l’utente, dopo la ricerca di un prodotto, accede alla
pagina contenente una lista del prodotto ricercato offerto dai diversi siti, con le relative informazioni. Si potrà cliccare su quello desiderato per recarsi sul sito di appartenenza del prodotto.



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
