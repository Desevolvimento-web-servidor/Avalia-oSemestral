from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from . import db, login_manager

class Semestre(db.Model):
    __tablename__ = 'semestres'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(32), unique=True, nullable=False)
    disciplinas = db.relationship('Disciplina', backref='semestre', lazy='dynamic')

    def __repr__(self):
        return f'<Semestre {self.nome}>'


class Disciplina(db.Model):
    __tablename__ = 'disciplinas'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    semestre_id = db.Column(db.Integer, db.ForeignKey('semestres.id'), nullable=False)

    def __repr__(self):
        return f'<Disciplina {self.nome}>'

