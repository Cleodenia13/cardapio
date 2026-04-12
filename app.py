from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # 👈 TEM QUE VIR PRIMEIRO

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cardapio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    preco = db.Column(db.Float)
    imagem = db.Column(db.String(300))
    