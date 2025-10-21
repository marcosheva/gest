# Gestionale Magazzino

Un'applicazione web Flask per la gestione del magazzino con database MongoDB.

## Funzionalità

- ✅ Aggiunta prodotti
- ✅ Visualizzazione prodotti
- ✅ Modifica quantità prodotti
- ✅ Rimozione prodotti
- ✅ Interfaccia responsive con Bootstrap

## Deployment su Render

### Prerequisiti
- Account Render (gratuito)
- Repository GitHub con il codice

### Passaggi per il deployment

1. **Prepara il repository GitHub:**
   ```bash
   git add .
   git commit -m "Preparazione per Render"
   git push origin main
   ```

2. **Vai su Render:**
   - Visita [render.com](https://render.com)
   - Fai login con GitHub

3. **Crea un nuovo Web Service:**
   - Clicca "New" → "Web Service"
   - Connetti il tuo repository GitHub
   - Seleziona il branch `main`

4. **Configura il servizio:**
   - **Name**: `gestionale-magazzino` (o nome a tua scelta)
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn gest:app`

5. **Imposta le variabili d'ambiente:**
   - Clicca su "Environment"
   - Aggiungi: `MONGO_URI` = `mongodb+srv://bet365odds:Aurora86@cluster0.svytet0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0`

6. **Deploy:**
   - Clicca "Create Web Service"
   - Render inizierà automaticamente il build e deploy

### Debug su Render

Se riscontri errori:

1. **Verifica i logs:**
   - Vai nella dashboard Render
   - Clicca sulla tua app
   - Vai su "Logs"

2. **Testa gli endpoint:**
   - `/` - Homepage
   - `/health` - Status dell'app
   - `/test` - Test semplice
   - `/prodotti` - Lista prodotti

3. **Controlla la configurazione:**
   - `requirements.txt` deve contenere `gunicorn==21.2.0`
   - `render.yaml` è presente (opzionale)
   - Variabili d'ambiente impostate

### Vantaggi di Render

- ✅ **Gratuito** per progetti piccoli
- ✅ **Deploy automatico** da GitHub
- ✅ **HTTPS** incluso
- ✅ **Logs** facili da vedere
- ✅ **Variabili d'ambiente** semplici da gestire

## Struttura progetto

```
├── docs/
│   └── index.html       # Template principale
├── gest.py              # Applicazione Flask principale
├── requirements.txt     # Dipendenze Python
├── render.yaml          # Configurazione Render (opzionale)
└── README.md           # Questo file
```

## Tecnologie utilizzate

- **Backend:** Flask (Python)
- **Database:** MongoDB Atlas
- **Frontend:** HTML5, Bootstrap 5, JavaScript
- **Deployment:** Render, Gunicorn
