from flask import Flask, render_template, request, redirect

app = Flask(__name__)

cardapio = [
    {"nome": "Hambúrguer", "preco": 10},
    {"nome": "X-Burger", "preco": 12},
    {"nome": "Batata Frita", "preco": 8},
    {"nome": "Refrigerante", "preco": 5}
]

@app.route("/")
def index():
    return render_template("index.html", cardapio=cardapio)

@app.route("/pedido", methods=["POST"])
def pedido():
    itens = request.form.getlist("pedido")

    mensagem = "Olá, quero pedir:\n"
    for item in itens:
        mensagem += f"- {item}\n"

    # COLOCA SEU NÚMERO AQUI (com DDD)
    numero = "5585987235195"

    link = f"https://wa.me/{numero}?text={mensagem}"

    return redirect(link)

if __name__ == "__main__":
    app.run(debug=True)