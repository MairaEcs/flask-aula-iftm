from flask import Flask, jsonify #importações
import os

app = Flask(__name__) # criando o app


@app.route('/') # rotas
def index():
    return jsonify({"Mensagem": "Bom dia, Maira"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
