from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new1.db'
db = SQLAlchemy(app)

class Pesquisador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pesquisador_nome = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    animais = db.relationship('Animal', backref='owner', lazy=True)

    def __init__(self,pesquisador_nome):
        self.pesquisador_nome = pesquisador_nome

    def __repr__(self):
        return '<Pesquisador %r>' % self.pesquisador_nome

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal_nome = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    pesquisador_id = db.Column(db.Integer, db.ForeignKey('pesquisador.id'), nullable=False)
    

    def __init__(self,animal_nome):
        self.animal_nome = animal_nome

    def __repr__(self):
        return '<Animal %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post_animal', methods=['POST'])
def post_animal():
    task = Animal(request.form['animal'])
    
    db.session.add(task)
    db.session.commit()
    return render_template('index.html')


@app.route('/post_pesquisador', methods=['POST'])
def post_pesquisador():
    pesquisador = Pesquisador(request.form['pesquisador'])
    db.session.add(pesquisador)
    db.session.commit()
    return render_template('index.html')


@app.route('/delete/<int:id>') #MVC
def delete(id):
    task_to_delete = Animal.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update', methods=['GET', 'POST'])
def gerenciamento():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('update.html')

'''
@app.route('/update/<string:animal_nome>') #MVC
def update():
    if request.method == 'POST':
        pass
    else:
        return render_template('update.html')
'''
if __name__ == "__main__":
    app.run(debug=True)
