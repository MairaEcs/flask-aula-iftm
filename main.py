from flask import Flask, jsonify, render_template, request #importações
import os

app = Flask(__name__, template_folder="templates") # criando o app


@app.route('/') # rotas
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        return jsonify(request.form)
    elif request.method == 'GET':
        return jsonify({"mensagem" : "Utilize o formulário"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
