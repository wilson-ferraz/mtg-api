from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# 🔹 Conectar ao MongoDB
MONGO_URI = "mongodb+srv://mtgreadonly:readonlymtg@mtg.fc4tp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client["mtg_cdb"]
cards_collection = db["cards"]

@app.route('/card/<name>', methods=['GET'])
def get_card(name):
    """ Busca uma carta pelo nome """
    card = cards_collection.find_one({"name": name}, {"_id": 0})
    if card:
        return jsonify(card)
    return jsonify({"error": "Card not found"}), 404

@app.route('/health', methods=['GET'])
def health_check():
    """ Verifica se a API está rodando """
    return jsonify({"status": "API está online!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
