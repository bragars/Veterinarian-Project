from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'

db = SQLAlchemy(app)

class Parent(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(500))
	child = db.relationship('Child', backref='parent', useList=False)
	
class Child(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(500))
	parent_id = db.Column(db.Integer, db.ForeignKey('parent.id'))
