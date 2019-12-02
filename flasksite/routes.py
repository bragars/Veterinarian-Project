from flask import render_template, url_for, request, redirect
from flasksite import app
from flasksite import db
#from flasksite.forms import SalaForm
from flasksite.models import Animal, Pessoa, Sala, Projeto, Estante, Caixa, Animal

@app.route('/')
def index():
    return render_template('index.html')
'''
@app.route("/register")
def register():
    form = SalaForm()
    return render_template('register.html', title='Register', form=form)
'''
'''
@app.route('/delete/<int:id>') #MVC
def delete(id):
    task_to_delete = Animal.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'
'''
@app.route('/update', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('update.html')

@app.route('/pesquisa', methods=['GET', 'POST'])
def pesquisa():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('pesquisa.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('delete.html')

@app.route('/sala', methods=['GET', 'POST'])
def sala():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('sala.html')

@app.route('/post_sala', methods=['POST'])
def post_sala():
    sala_content = request.form['numero']
    sala = Sala(Numero=sala_content)
    db.session.add(sala)
    db.session.commit()
    return redirect(url_for('cadastro'))
    
@app.route('/pessoa', methods=['GET', 'POST'])
def pessoa():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('pessoa.html')

@app.route('/post_pessoa', methods=['POST'])
def post_pessoa():
    nome_content = request.form['nome']
    telefone_content = request.form['telefone']
    email_content = request.form['email']
    
    pessoa = Pessoa(nome=nome_content, telefone=telefone_content, email=email_content)
    db.session.add(pessoa)
    db.session.commit()
    
    return redirect(url_for('cadastro'))

@app.route('/projeto', methods=['GET', 'POST'])
def projeto():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('projeto.html')

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
    
    projeto = Projeto(Nome=Nome_content, CEUA=CEUA_content, Data_Exp_CEUA=Data_Exp_CEUA_content,
                      N_Animais_Aprovados=N_Animais_Aprovados_content, N_Animais_Bioterio=N_Animais_Bioterio_content, 
                      Data_Ent_Bioterio=Data_Ent_Bioterio_content,Data_Saida=Data_Saida_content, 
                      Motivo_Saida=Motivo_Saida_content, Status=Status_content,Descricao=Descricao_content)
    db.session.add(projeto)
    db.session.commit()
    
    return redirect(url_for('cadastro'))


@app.route('/estante', methods=['GET', 'POST'])
def estante():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('estante.html')

@app.route('/post_estante', methods=['POST'])
def post_estante():
    Patrimonio_content = request.form['Patrimonio']
    Sala_content = request.form['Sala_id']
    
    estante = Estante(Patrimonio=Patrimonio_content, Sala_id=Sala_content)
    db.session.add(estante)
    db.session.commit()
    
    return redirect(url_for('cadastro'))

@app.route('/caixa', methods=['GET', 'POST'])
def caixa():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('caixa.html')

@app.route('/post_caixa', methods=['POST'])
def post_caixa():
    Patrimonio_content = request.form['Patrimonio']
    Estante_content = request.form['Estante_id']
    Projeto_content = request.form['Projeto_id']
    
    caixa = Estante(Patrimonio=Patrimonio_content, Estante_id=Patrimonio_content, Projeto_id=Projeto_content)
    db.session.add(caixa)
    db.session.commit()
    
    return redirect(url_for('cadastro'))

@app.route('/animal', methods=['GET', 'POST'])
def animal():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('animal.html')

@app.route('/post_animal', methods=['POST'])
def post_animal():
    Patrimonio_content = request.form['Patrimonio']
    especie_content = request.form['especie']
    linhagem_content = request.form['linhagem']
    sexo_content = request.form['sexo']
    nascimento_content = request.form['nascimento']
    Caixa_content = request.form['Caixa_id']
    
    animal = Estante(Patrimonio=Patrimonio_content, Estante_id=Patrimonio_content, Projeto_id=Projeto_content)
    db.session.add(animal)
    db.session.commit()
    
    return redirect(url_for('cadastro'))

'''
@app.route('/update/<string:animal_nome>') #MVC
def update():
    if request.method == 'POST':
        pass
    else:
        return render_template('update.html')
'''