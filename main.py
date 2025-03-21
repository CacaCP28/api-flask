from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/consumir-api', methods=['GET'])
def consumir_api():
    url = "https://api.conecttec.com.br/V7/ForecourtMap/ById/2837"
    headers = {
        "SecretKeyAuthorization": "53c30b89-f192-49a8-808b-05596fec4d1f"
    }

    # Realiza a requisição GET à API
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return jsonify(response.json())  # Retorna os dados em JSON
    else:
        return jsonify({"erro": "Erro ao consumir a API"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Isso torna o link acessível
