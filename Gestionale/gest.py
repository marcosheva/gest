from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

# Connessione al database MongoDB
MONGO_URI = "mongodb+srv://bet365odds:Aurora86@cluster0.svytet0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=False)
db = client["libreria"]
collezione_prodotti = db["prodotti"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aggiungi_prodotto', methods=['POST'])
def aggiungi_prodotto():
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

@app.route('/prodotti', methods=['GET'])
def get_prodotti():
    prodotti = list(collezione_prodotti.find({}, {"_id": 0}))  # Prendi tutti i prodotti senza l'ID
    return jsonify(prodotti)

@app.route('/modifica_prodotto', methods=['POST'])
def modifica_prodotto():
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

@app.route('/rimuovi_prodotto', methods=['POST'])
def rimuovi_prodotto():
    nome_prodotto = request.form.get('nome')

    if nome_prodotto:
        result = collezione_prodotti.delete_one({'nome': nome_prodotto})
        
        if result.deleted_count > 0:
            return jsonify({"success": True, "message": f"Prodotto '{nome_prodotto}' rimosso con successo."})
        else:
            return jsonify({"success": False, "message": "Prodotto non trovato."})
    return jsonify({"success": False, "message": "Nome prodotto non fornito."})



if __name__ == '__main__':
    app.run(debug=True)
