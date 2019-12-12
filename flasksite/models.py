from datetime import datetime
from flasksite import db

class Caixa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Patrimonio = db.Column(db.String(200), nullable=False)
    Estante_id = db.Column(db.Integer, db.ForeignKey('estante.id'), nullable=True)
    animais = db.relationship('Animal', backref='owner', lazy=True)
    Projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id'), nullable=True)
    def __repr__(self):
        return '<Caixa %r>' % self.id
    
    
class Estante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Patrimonio = db.Column(db.String(200), nullable=False)
    Sala_id = db.Column(db.Integer, db.ForeignKey('sala.id'), nullable=True)
    caixas = db.relationship('Caixa', backref='owner', lazy=True)
    def __repr__(self):
        return '<Estante %r>' % self.id


class Sala(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Numero = db.Column(db.Integer, nullable=False)
    estantes = db.relationship('Estante', backref='owner', lazy=True)    
    def __repr__(self):
        return '<Sala %r>' % self.id
    
class Projeto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    CEUA = db.Column(db.Integer) 
    Data_Exp_CEUA = db.Column(db.Integer)
    N_Animais_Aprovados = db.Column(db.Integer)
    N_Animais_Bioterio = db.Column(db.Integer)
    Data_Ent_Bioterio = db.Column(db.Integer)
    Data_Saida = db.Column(db.Integer)  
    Motivo_Saida = db.Column(db.String(200), nullable=False)
    Status = db.Column(db.String(200), nullable=False)
    Nome = db.Column(db.String(200), nullable=False)
    Descricao = db.Column(db.String(200), nullable=False)
    
    caixas_projeto = db.relationship('Caixa', backref='Projeto', lazy=True)
    def __repr__(self):
        return '<Caixa %r>' % self.id

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    especie = db.Column(db.String(200), nullable=False)
    linhagem = db.Column(db.String(200), nullable=False)
    sexo = db.Column(db.String(200), nullable=False)
    nascimento = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    Caixa_id = db.Column(db.Integer, db.ForeignKey('caixa.id'), nullable=True)
    def __repr__(self):
        return '<Animal %r>' % self.id


responsavel = db.Table('responsavel',
    db.Column('pessoa_id', db.Integer, db.ForeignKey('pessoa.id')),
    db.Column('sala_id',   db.Integer, db.ForeignKey('sala.id'))
)

encarregado = db.Table('encarregado',
    db.Column('pessoa_id', db.Integer, db.ForeignKey('pessoa.id')),
    db.Column('projeto_id',   db.Integer, db.ForeignKey('projeto.id'))
)

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    responsabilidade = db.relationship('Sala', secondary=responsavel, backref=db.backref('responsaveis', lazy='dynamic'))    
    encarregar = db.relationship('Projeto', secondary=encarregado, backref=db.backref('encarregados', lazy='dynamic'))
    #TYPE ENUM - PESQUISADOR, ALUNO RESPONSAVEL, OUTROS COLABORADORES, ADMIN
    def __repr__(self):
        return '<Pessoa %r>' % self.id