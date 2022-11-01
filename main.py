from flask import Flask, jsonify, render_template #importações
import os

app = Flask(__name__, template_folder="templates") # criando o app


@app.route('/') # rotas
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
