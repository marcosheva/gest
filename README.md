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

### Risoluzione problemi

Se riscontri errori 404 o problemi di caricamento dati:

1. **Verifica i logs:**
   ```bash
   heroku logs --tail
   ```

2. **Controlla che gunicorn sia installato:**
   Il file `requirements.txt` deve contenere `gunicorn==21.2.0`

3. **Verifica il Procfile:**
   Deve contenere: `web: gunicorn gest:app`

4. **Testa localmente:**
   ```bash
   python gest.py
   ```

## Struttura progetto

```
├── gest.py              # Applicazione Flask principale
├── templates/
│   └── index.html       # Interfaccia utente
├── requirements.txt     # Dipendenze Python
├── Procfile            # Configurazione Heroku
└── README.md           # Questo file
```

## Tecnologie utilizzate

- **Backend:** Flask (Python)
- **Database:** MongoDB Atlas
- **Frontend:** HTML5, Bootstrap 5, JavaScript
- **Deployment:** Heroku, Gunicorn
