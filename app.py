from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # 👈 TEM que vir antes de tudo

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cardapio.db'
db = SQLAlchemy(app)
@app.route('/')
def index():
    produtos = Produto.query.all()
    return render_template('index.html', produtos=produtos)
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = float(request.form['preco'])
        imagem = request.form['imagem']

        novo = Produto(nome=nome, preco=preco, imagem=imagem)
        db.session.add(novo)
        db.session.commit()

        return redirect('/admin')

    produtos = Produto.query.all()
    return render_template('admin.html', produtos=produtos)