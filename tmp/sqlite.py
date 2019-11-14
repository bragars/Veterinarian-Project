import sqlite3

class User:
     def __init__(self, cpf, name, email, password):
        self.name = name
        self.cpf = cpf
        self.email = email
        self.password = password

connection = sqlite3.connect('user.db')

c = connection.cursor()

User.name = input('Digite o nome')
User.cpf = input('Digite o cpf')
User.email = input('Digite o email')
User.password = input('Digite o password')


def insert_user(user_values):
        with connection:
                c.execute("""INSERT INTO users VALUES(:name, :cpf, :email, :password)""", user_values)


user_values = {'name': User.name, 'cpf': User.cpf, 'email': User.email, 'password': User.password}

insert_user(user_values)

connection.commit()
connection.close()



















'''
from user import User

import sqlite3

connection = sqlite3.connect('Place.db')

c = connection.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS dados (id integer, unix real,keyword text, \
        datestamp text, value real)')#unix valor decimal
    
create_table()

def dataentry():
    c.execute("INSERT INTO dados VALUES(1, 10, 'Python Sentiment', \
    '2013-04-14 10:09:41',2) ")
    c.execute("INSERT INTO dados VALUES(1, 10, 'Mickaela', \
    '2013-04-14 10:09:41',5) ")
    c.execute("INSERT INTO dados VALUES(1, 10, 'Maravilhosa', \
    '2013-04-14 10:09:41',8) ")
    
    connection.commit()#PRECISA DO COMMIT PARA REALMENTE ESCREVER NO Db
    
dataentry() 
    
#print(c.fetchall())    

'''