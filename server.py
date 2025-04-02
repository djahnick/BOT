from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Chemin absolu vers le dossier Files de MT5
MT5_FILES_PATH = r"/Users/djahnickefrei/Library/Application Support/net.metaquotes.wine.metatrader5/drive_c/Program Files/MetaTrader 5/MQL5/Files/alert.json"

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    print("Alerte reçue :", data)
    
    # Générer un JSON compact
    json_content = json.dumps(data, separators=(',', ':'))
    # Encoder le JSON en CP1252
    json_bytes = json_content.encode('cp1252')
    
    # Écriture en mode binaire dans le dossier Files de MT5
    with open(MT5_FILES_PATH, 'wb') as f:
        f.write(json_bytes)
        
    return jsonify({"status": "success", "message": "Alerte reçue"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
