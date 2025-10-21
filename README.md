# Gestionale Magazzino

Un'applicazione web Flask per la gestione del magazzino con database MongoDB.

## Funzionalità

- ✅ Aggiunta prodotti
- ✅ Visualizzazione prodotti
- ✅ Modifica quantità prodotti
- ✅ Rimozione prodotti
- ✅ Interfaccia responsive con Bootstrap

## Deployment su Heroku

### Prerequisiti
- Account Heroku
- Git installato
- Heroku CLI installato

### Passaggi per il deployment

1. **Crea un'app Heroku:**
   ```bash
   heroku create nome-tua-app
   ```

2. **Imposta le variabili d'ambiente (opzionale):**
   ```bash
   heroku config:set MONGO_URI="mongodb+srv://bet365odds:Aurora86@cluster0.svytet0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
   ```

3. **Deploy del codice:**
   ```bash
   git add .
   git commit -m "Deploy gestionale magazzino"
   git push heroku main
   ```

4. **Apri l'applicazione:**
   ```bash
   heroku open
   ```

### Debug su Heroku

Se riscontri errori 404 o problemi di caricamento dati:

1. **Verifica i logs:**
   ```bash
   heroku logs --tail
   ```

2. **Testa l'endpoint di health:**
   ```bash
   curl https://nome-tua-app.herokuapp.com/health
   ```

3. **Verifica che tutti gli endpoint siano accessibili:**
   - `/` - Homepage
   - `/health` - Status dell'app
   - `/prodotti` - Lista prodotti (GET)
   - `/aggiungi_prodotto` - Aggiungi prodotto (POST)
   - `/modifica_prodotto` - Modifica prodotto (POST)
   - `/rimuovi_prodotto` - Rimuovi prodotto (POST)

4. **Controlla la configurazione:**
   - `requirements.txt` deve contenere `gunicorn==21.2.0`
   - `Procfile` deve contenere: `web: gunicorn gest:app`
   - `runtime.txt` specifica la versione Python

### Risoluzione problemi comuni

**Errore 404 su `/prodotti`:**
- Verifica che l'app sia deployata correttamente
- Controlla i logs per errori di connessione MongoDB
- Testa l'endpoint `/health` per verificare lo stato

**Database non disponibile:**
- Verifica la connessione MongoDB Atlas
- Controlla che l'IP di Heroku sia whitelisted su MongoDB Atlas
- Verifica le credenziali di connessione

## Struttura progetto

```
├── docs/
│   └── index.html       # Template principale
├── gest.py              # Applicazione Flask principale
├── requirements.txt     # Dipendenze Python
├── Procfile            # Configurazione Heroku
├── runtime.txt         # Versione Python per Heroku
└── README.md           # Questo file
```

## Tecnologie utilizzate

- **Backend:** Flask (Python)
- **Database:** MongoDB Atlas
- **Frontend:** HTML5, Bootstrap 5, JavaScript
- **Deployment:** Heroku, Gunicorn
