from enum import unique
from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import backref
from db import DB

app = Flask(__name__)
db = DB(app)
ma = Marshmallow(app)

# Definicion y Creacion llaves foraneas
class Perfil(db.db.Model):
    __tablename__ = 'perfil'
    idPerfil = db.db.Column(db.db.Integer, primary_key=True, autoincrement=True, unique=True)
    nombre = db.db.Column(db.db.String(50))
    apodo = db.db.Column(db.db.String(50), unique=True)
    correo = db.db.Column(db.db.String(50), unique=True)
    password = db.db.Column(db.db.String(50))


class Chat(db.db.Model):
    __tablename__ = 'chat'
    idChat = db.db.Column(db.db.Integer, primary_key=True, autoincrement=True)
    conversacion = db.db.Column(db.db.JSON)
    perfil_id = db.db.Column(db.db.Integer, db.db.ForeignKey('perfil.idPerfil'))
    perfil = db.db.relationship('Perfil', backref=db.db.backref('Chat'))


class Galeria(db.db.Model):
    __tablename__ = 'galeria'
    idGaleria = db.db.Column(db.db.Integer, primary_key=True,)
    JPG = db.db.Column(db.db.BLOB)
    perfil_id = db.db.Column(db.db.Integer, db.db.ForeignKey('perfil.idPerfil'))
    perfil = db.db.relationship('Perfil', backref=db.db.backref('Galeria'))

        
class Conversatorio(db.db.Model):
    __tablename__ = 'conversatorio'
    idConversatorio = db.db.Column(db.db.Integer, primary_key=True, autoincrement=True)
    pregunta = db.db.Column(db.db.String(250))
    perfil_id = db.db.Column(db.db.Integer, db.db.ForeignKey('perfil.idPerfil'))
    perfil = db.db.relationship('Perfil', backref=db.db.backref('Conversatorio'))
        

class Respuesta(db.db.Model):
    __tablename__ = 'respuesta'
    idRespuesta = db.db.Column(db.db.Integer, primary_key=True, autoincrement=True)
    respuesta = db.db.Column(db.db.String(250))
    conversatorio_id = db.db.Column(db.db.Integer, db.db.ForeignKey('conversatorio.idConversatorio'))
    conversatorio = db.db.relationship('Conversatorio', backref=db.db.backref('Respuesta'))


db.db.create_all()

@app.route('/', methods=['GET'])
def index():
    nuevo_perfil = Perfil(nombre='Juanito', apodo="ito", correo="bdsrt@sgds.com", password='1234')
    db.db.session.add(nuevo_perfil)
    db.db.session.commit()

    return db.db.session.query(Perfil).all()




if __name__ == "__main__":
    app.run(debug=True)

                 