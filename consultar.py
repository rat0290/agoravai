from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__, template_folder=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates'))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        telefone = request.form["telefone"]
        cpf = encontrar_cpf_por_telefone(telefone)
        if cpf:
            dados_api = consultar_api_cpf(cpf)
            if dados_api:
                return render_template("index.html", cpf=cpf, telefone=telefone, dados=dados_api)
            else:
                return render_template("index.html", erro="Não foi possível consultar os dados na API.")
        else:
            return render_template("index.html", erro="Telefone não encontrado.")
    return render_template("index.html")

def handler(request):
    with app.app_context():
        return app.full_dispatch_request()

if __name__ == "__main__":
    app.run(debug=True)
