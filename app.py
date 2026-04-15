from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # 👈 TEM que vir antes de tudo

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cardapio.db'
db = SQLAlchemy(app)
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    preco = db.Column(db.Float)
    imagem = db.Column(db.String(300))
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
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    class Loja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    slug = db.Column(db.String(100), unique=True)
    logo = db.Column(db.String(300))
    whatsapp = db.Column(db.String(20))
    pix = db.Column(db.String(100))
    class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    preco = db.Column(db.Float)
    imagem = db.Column(db.String(300))
    loja_id = db.Column(db.Integer, db.ForeignKey('loja.id'))
    @app.route('/<slug>')
def loja(slug):
    loja = Loja.query.filter_by(slug=slug).first()
    produtos = Produto.query.filter_by(loja_id=loja.id).all()

    return render_template('loja.html', loja=loja, produtos=produtos)