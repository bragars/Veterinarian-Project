from flask import Flask, 

# Configuração baseada em classe
class ConfigClass(object):

    # Configurações do Flask-SQLAlchemy 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///basic_app.sqlite'   
    SQLALCHEMY_TRACK_MODIFICATIONS = False   

def create_app():
    
    # Cria um app FLask
    app = Flask(__name__)
    # Carrega as configurações criadas na classe acima
    # app.config.from_object(__name__+'.ConfigClass')

    # Initialize Flask-SQLAlchemy
    db = SQLAlchemy(app)

    return app

# Inicializar o servidor de desenvolvimento
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)