from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

app = Flask(__name__)
CORS(app)

# Connexion à MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify({"message": "Salut nouvelle apps!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
