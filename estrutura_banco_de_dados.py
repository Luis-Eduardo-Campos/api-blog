from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Criar um API flask
app = Flask(__name__)
# Criar uma instância de SQLAlchemy
app.config['SECRET_KEY'] = 'SWKID0099#'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:namdjKxN2ejxFGCBUOO2@containers-us-west-22.railway.app:5993/railway'

db = SQLAlchemy(app)
db:SQLAlchemy
# Definir a estrutura da tabela Postagem
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))
# Definir a estrutura da tabela Autor
# id_autor, nome, email, senha, admin, postagens
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')


def inicializar_banco():
    with app.app_context():
        # Executar o comando para criar o banco de dados
        db.drop_all()
        db.create_all()
        # Criar usuários administradores
        autor = Autor(nome='Luis', email='bolota@gmail.com', senha='luffy3276', admin=True)
        db.session.add(autor)
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        inicializar_banco()