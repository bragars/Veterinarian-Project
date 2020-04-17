from flask import render_template, url_for, request, redirect
from flasksite import app
from flasksite import db
#from flasksite.forms import SalaForm
from flasksite.models import Animal, Pessoa, Sala, Projeto, Estante, Caixa, Animal
# flask API
# JSON   { "nome": "oi"}
# test automatizados (unitarios e ponta a ponta) com pyunit pytest
# cobertura de  codigo
# front VueJS x React X Angular
# laracast vue 2, youtube: academind
# travis CI
# devops  back end  front end designer
@app.route('/')
def index():
    return render_template('index.html')
#
@app.route('/update', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))
    # show the form, it wasn't submitted
    return render_template('update.html')
#
@app.route('/pesquisa', methods=['GET', 'POST'])
def pesquisa():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('pesquisa.html')
#
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        return redirect(url_for('index'))
#
    return render_template('delete.html')
#
@app.route('/sala', methods=['GET', 'POST'])
def sala():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('sala.html')
#
@app.route('/post_sala', methods=['POST'])
def post_sala():
    sala_content = request.form['numero']
    nome_content = request.form['nome']
    sala = Sala(Numero=sala_content)
    db.session.add(sala)
    db.session.commit()
    if nome_content:
        pessoa = Pessoa.query.filter_by(nome=nome_content).first()
        sala.responsaveis.append(pessoa)
        db.session.commit()
    return redirect(url_for('cadastro'))
#
@app.route('/pesquisa_sala', methods=['GET', 'POST'])
def pesquisa_sala():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('pesquisa_sala.html')
#
@app.route('/pesquisar_sala', methods=['POST'])
def pesquisar_sala():
    sala_content = request.form['numero']
    if sala_content:
        search = Sala.query.filter_by(Numero=sala_content).first()
        if search:
            return render_template('pesquisa_sala.html',search=search)
        else:
            return render_template('pesquisa_sala.html',search=search)
    else:
        return "hello"

@app.route('/delete_sala', methods=['GET', 'POST'])
def delete_sala():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('delete_sala.html')
#
@app.route('/deletar_sala', methods=['POST'])
def deletar_sala():
    numero_content = request.form['numero']
    search = Sala.query.filter_by(Numero=numero_content).first()
    db.session.delete(search)
    db.session.commit()
    return render_template('delete_sala.html')
#
@app.route('/pessoa', methods=['GET', 'POST'])
def pessoa():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('pessoa.html')
#
@app.route('/post_pessoa', methods=['POST'])
def post_pessoa():
    nome_content = request.form['nome']
    telefone_content = request.form['telefone']
    email_content = request.form['email']
    pessoa = Pessoa(nome=nome_content, telefone=telefone_content, email=email_content)
    db.session.add(pessoa)
    db.session.commit()
    return redirect(url_for('cadastro'))
#
@app.route('/pesquisa_pessoa', methods=['GET', 'POST'])
def pesquisa_pessoa():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('pesquisa_pessoa.html')
#
@app.route('/pesquisar_pessoa', methods=['POST'])
def pesquisar_pessoa():
    nome_content = request.form['nome']
    if nome_content:
        search = Pessoa.query.filter_by(nome=nome_content).first()
        if search:
            return render_template('pesquisa_pessoa.html',search=search)
        else:
            return render_template('pesquisa_pessoa.html',search=search)
    else:
        return "hello"
#
@app.route('/delete_pessoa', methods=['GET', 'POST'])
def delete_pessoa():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('delete_pessoa.html')
#
@app.route('/deletar_pessoa', methods=['POST'])
def deletar_pessoa():
    nome_content = request.form['nome']
    search = Pessoa.query.filter_by(nome=nome_content).first()
    db.session.delete(search)
    db.session.commit()
    return render_template('delete_sala.html')
#
@app.route('/projeto', methods=['GET', 'POST'])
def projeto():
    if request.method == 'POST':
        return redirect(url_for('index'))
#
    return render_template('projeto.html')
#
@app.route('/post_projeto', methods=['POST'])
def post_projeto():
    Nome_content = request.form['Nome']
    CEUA_content = request.form['CEUA']
    Data_Exp_CEUA_content = request.form['Data_Exp_CEUA']
    N_Animais_Aprovados_content = request.form['N_Animais_Aprovados']
    N_Animais_Bioterio_content = request.form['N_Animais_Bioterio']
    Data_Ent_Bioterio_content = request.form['Data_Ent_Bioterio']
    Data_Saida_content = request.form['Data_Saida']
    Motivo_Saida_content = request.form['Motivo_Saida']
    Status_content = request.form['Status']
    Descricao_content = request.form['Descricao']
    responsavel_content = request.form['responsavel']
    projeto = Projeto(Nome=Nome_content, CEUA=CEUA_content, Data_Exp_CEUA=Data_Exp_CEUA_content,
                      N_Animais_Aprovados=N_Animais_Aprovados_content, N_Animais_Bioterio=N_Animais_Bioterio_content,
                      Data_Ent_Bioterio=Data_Ent_Bioterio_content,Data_Saida=Data_Saida_content,
                      Motivo_Saida=Motivo_Saida_content, Status=Status_content,Descricao=Descricao_content)
#
    db.session.add(projeto)
    db.session.commit()
#
    pessoa = Pessoa.query.filter_by(nome=responsavel_content).first()
    projeto.encarregados.append(pessoa)
    db.session.commit()
    return redirect(url_for('cadastro'))
#
@app.route('/pesquisa_projeto', methods=['GET', 'POST'])
def pesquisa_projeto():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('pesquisa_projeto.html')
#
@app.route('/pesquisar_projeto', methods=['POST'])
def pesquisar_projeto():
    nome_content = request.form['nome']
    if nome_content:
        search = Projeto.query.filter_by(Nome=nome_content).first()
        if search:
            return render_template('pesquisa_projeto.html',search=search)
        else:
            return render_template('pesquisa_projeto.html',search=search)
    else:
        return "hello"
#
@app.route('/delete_projeto', methods=['GET', 'POST'])
def delete_projeto():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('delete_projeto.html')
#
@app.route('/deletar_projeto', methods=['POST'])
def deletar_projeto():
    nome_content = request.form['nome']
    search = Projeto.query.filter_by(Nome=nome_content).first()
    db.session.delete(search)
    db.session.commit()
    return render_template('delete_projeto.html')

@app.route('/estante', methods=['GET', 'POST'])
def estante():
    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('estante.html')

@app.route('/post_estante', methods=['POST'])
def post_estante():
    Patrimonio_content = request.form['Patrimonio']
    Sala_content = request.form['Sala_id']
    sala = Sala.query.filter_by(Numero=Sala_content).first()
    estante = Estante(Patrimonio=Patrimonio_content, Sala_id=sala.id)
    db.session.add(estante)
    db.session.commit()
    return redirect(url_for('cadastro'))

@app.route('/pesquisa_estante', methods=['GET', 'POST'])
def pesquisa_estante():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('pesquisa_estante.html')

@app.route('/pesquisar_estante', methods=['POST'])
def pesquisar_estante():
    nome_content = request.form['nome']
    if nome_content:
        search = Estante.query.filter_by(Patrimonio=nome_content).first()
        if search:
            return render_template('pesquisa_estante.html',search=search)
        else:
            return render_template('pesquisa_estante.html',search=search)
    else:
        return "hello"

@app.route('/delete_estante', methods=['GET', 'POST'])
def delete_estante():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('delete_estante.html')

@app.route('/deletar_estante', methods=['POST'])
def deletar_estante():
    patrimonio_content = request.form['nome']
    search = Estante.query.filter_by(Patrimonio=patrimonio_content).first()
    db.session.delete(search)
    db.session.commit()
    return render_template('delete_estante.html')


@app.route('/caixa', methods=['GET', 'POST'])
def caixa():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('caixa.html')

@app.route('/post_caixa', methods=['POST'])
def post_caixa():
    Patrimonio_content = request.form['Patrimonio']
    Estante_content = request.form['Estante_id']
    estante = Estante.query.filter_by(Patrimonio=Estante_content).first()
    Projeto_content = request.form['Projeto_id']
    projeto = Projeto.query.filter_by(Nome=Projeto_content).first()
    caixa = Caixa(Patrimonio=Patrimonio_content, Estante_id=estante.id, Projeto_id=projeto.id)
    db.session.add(caixa)
    db.session.commit()
    return redirect(url_for('cadastro'))

@app.route('/pesquisa_caixa', methods=['GET', 'POST'])
def pesquisa_caixa():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('pesquisa_caixa.html')

@app.route('/pesquisar_caixa', methods=['POST'])
def pesquisar_caixa():
    nome_content = request.form['nome']
    if nome_content:
        search = Caixa.query.filter_by(Patrimonio=nome_content).first()
        if search:
            return render_template('pesquisa_caixa.html',search=search)
        else:
            return render_template('pesquisa_caixa.html',search=search)
    else:
        return "hello"

@app.route('/delete_caixa', methods=['GET', 'POST'])
def delete_caixa():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('delete_caixa.html')

@app.route('/deletar_caixa', methods=['POST'])
def deletar_caixa():
    patrimonio_content = request.form['nome']
    search = Caixa.query.filter_by(Patrimonio=patrimonio_content).first()
    db.session.delete(search)
    db.session.commit()
    return render_template('delete_caixa.html')


@app.route('/animal', methods=['GET', 'POST'])
def animal():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('animal.html')

@app.route('/post_animal', methods=['POST'])
def post_animal():
    especie_content = request.form['especie']
    linhagem_content = request.form['linhagem']
    sexo_content = request.form['sexo']
    nascimento_content = request.form['nascimento']
    Caixa_content = request.form['Caixa_id']
    caixa = Caixa.query.filter_by(Patrimonio=Caixa_content).first()
    animal = Animal(especie=especie_content, linhagem=linhagem_content,
                    sexo=sexo_content, nascimento=nascimento_content,Caixa_id=caixa.id)
    db.session.add(animal)
    db.session.commit()

    return redirect(url_for('cadastro'))

@app.route('/pesquisa_animal', methods=['GET', 'POST'])
def pesquisa_animal():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('pesquisa_animal.html')

@app.route('/pesquisar_animal', methods=['POST'])
def pesquisar_animal():
    nome_content = request.form['nome']
    if nome_content:
        search = Animal.query.filter_by(especie=nome_content).first()
        if search:
            return render_template('pesquisa_animal.html',search=search)
        else:
            return render_template('pesquisa_animal.html',search=search)
    else:
        return "hello"

@app.route('/delete_animal', methods=['GET', 'POST'])
def delete_animal():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('delete_animal.html')
#
@app.route('/deletar_animal', methods=['POST'])
def deletar_animal():
    nome_content = request.form['nome']
    search = Animal.query.filter_by(especie=nome_content).first()
    #search_1 = responsavel.query.filter_by(pessoa_id=nome_content).first()
    #search_2 = encarregado.query.filter_by(projeto_id=nome_content).first()
    db.session.delete(search)
    db.session.commit()
    return render_template('delete_animal.html')
