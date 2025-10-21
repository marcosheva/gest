from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import json
import os

app = Flask(__name__, template_folder='docs')

# Configurazione per Heroku
port = int(os.environ.get('PORT', 5000))

# Connessione al database MongoDB
MONGO_URI = os.environ.get('MONGO_URI', "mongodb+srv://bet365odds:Aurora86@cluster0.svytet0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

try:
    client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=False)
    db = client["libreria"]
    collezione_prodotti = db["prodotti"]
    # Test della connessione
    client.admin.command('ping')
    print("✅ Connessione a MongoDB riuscita!")
except Exception as e:
    print(f"❌ Errore connessione MongoDB: {e}")
    client = None
    db = None
    collezione_prodotti = None

@app.route('/')
def index():
    print("🔍 Accesso alla homepage")
    return render_template('index.html')

@app.route('/health')
def health():
    """Endpoint di test per verificare che l'app funzioni"""
    return jsonify({
        "status": "ok", 
        "database": "connected" if collezione_prodotti is not None else "disconnected",
        "port": port
    })

@app.route('/aggiungi_prodotto', methods=['POST'])
def aggiungi_prodotto():
    if collezione_prodotti is None:
        return jsonify({"message": "❌ Database non disponibile!", "success": False})
    
    try:
        nome = request.form['nome']
        marca = request.form['marca']
        quantita = int(request.form['quantita'])

        # Verifica se il prodotto esiste già nel database
        prodotto_esistente = collezione_prodotti.find_one({"nome": nome})
        
        if prodotto_esistente:
            return jsonify({"message": "❌ Prodotto già esistente!", "success": False})

        # Aggiungi nuovo prodotto
        collezione_prodotti.insert_one({
            "nome": nome,
            "marca": marca,
            "quantita": quantita
        })

        return jsonify({"message": f"✅ Prodotto '{nome}' aggiunto con successo!", "success": True})
    except Exception as e:
        return jsonify({"message": f"❌ Errore: {str(e)}", "success": False})

@app.route('/prodotti', methods=['GET'])
def get_prodotti():
    print("🔍 Richiesta prodotti ricevuta")
    if collezione_prodotti is None:
        print("❌ Database non disponibile")
        return jsonify({"error": "Database non disponibile"}), 500
    
    try:
        print("🔍 Recupero prodotti dal database")
        prodotti = list(collezione_prodotti.find({}, {"_id": 0}))  # Prendi tutti i prodotti senza l'ID
        print(f"✅ Trovati {len(prodotti)} prodotti")
        return jsonify(prodotti)
    except Exception as e:
        print(f"❌ Errore nel caricamento prodotti: {str(e)}")
        return jsonify({"error": f"Errore nel caricamento prodotti: {str(e)}"}), 500

@app.route('/modifica_prodotto', methods=['POST'])
def modifica_prodotto():
    if collezione_prodotti is None:
        return jsonify({"message": "❌ Database non disponibile!", "success": False})
    
    try:
        nome = request.form['nome']
        quantita = int(request.form['quantita'])

        # Verifica se il prodotto esiste nel database
        prodotto_esistente = collezione_prodotti.find_one({"nome": nome})

        if prodotto_esistente:
            # Aggiorna la quantità del prodotto
            collezione_prodotti.update_one(
                {"nome": nome},
                {"$set": {"quantita": quantita}}
            )
            return jsonify({"message": f"✅ Quantità del prodotto '{nome}' aggiornata a {quantita}.", "success": True})
        else:
            return jsonify({"message": "❌ Prodotto non trovato.", "success": False})
    except Exception as e:
        return jsonify({"message": f"❌ Errore: {str(e)}", "success": False})

@app.route('/rimuovi_prodotto', methods=['POST'])
def rimuovi_prodotto():
    if collezione_prodotti is None:
        return jsonify({"success": False, "message": "❌ Database non disponibile!"})
    
    try:
        nome_prodotto = request.form.get('nome')

        if nome_prodotto:
            result = collezione_prodotti.delete_one({'nome': nome_prodotto})
            
            if result.deleted_count > 0:
                return jsonify({"success": True, "message": f"Prodotto '{nome_prodotto}' rimosso con successo."})
            else:
                return jsonify({"success": False, "message": "Prodotto non trovato."})
        return jsonify({"success": False, "message": "Nome prodotto non fornito."})
    except Exception as e:
        return jsonify({"success": False, "message": f"❌ Errore: {str(e)}"})



if __name__ == '__main__':
    print(f"🚀 Avvio server Flask su porta {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
