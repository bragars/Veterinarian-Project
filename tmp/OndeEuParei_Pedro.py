
import sqlite3

connection = sqlite3.connect('user.db')

c = connection.cursor()


c.execute("CREATE TABLE IF NOT EXISTS animals(name, name1, name2, name3)")


def insert_user(user_values):
        with connection:
                c.execute("""INSERT INTO users VALUES(:name, :name1, :name2, :name3)""", user_values)


class animal:
    def __init__(self, especie, linhagem, sexo, nascimento):
        self.especie = especie
        self.linhagem = linhagem
        self.sexo = sexo
        self.nascimento = nascimento

class aluno:
    def __init__(self, nome, vinculo_Institucional, email, telefone):
        self.nome = nome
        self.vinculo_Institucional = vinculo_Institucional
        self.email = email
        self.telefone = telefone

class outros_colaboradores:
    def __init__(self, nome, vinculo_Institucional, email, telefone):
        self.nome = nome
        self.vinculo_Institucional = vinculo_Institucional
        self.email = email
        self.telefone = telefone

class pesquisador:
    def __init__(self, contato, email, laboratorio, centro_de_custo):
        self.contato = contato
        self.email = email
        self.laboratorio = laboratorio
        self.centro_de_custo = centro_de_custo

def main():
    print("== Menu ==")
    print("1 - Cadastro de animal(ais)")
    print("2 - Cadastro de aluno(a)")
    print("3 - Cadastro de outro colaborador(es)")
    print("4 - Cadastro de pesquisador(es)")
    print("0 - Sair")

    option = int(input())

    if(option == 1):
        n = int(input('Entre com o número de animal(ais): '))
        for i in range(n):
            animal.especie =  input('Digite a especie : ')
            animal.linhagem = input('Digite a linhagem : ')
            animal.sexo = input('Digite o sexo : ')
            animal.nascimento = input('Digite o nascimento : ')

            especie = animal.especie
            linhagem =animal.linhagem
            sexo = animal.sexo
            nascimento = animal.nascimento
            
            animal(animal.especie,animal.linhagem, animal.sexo,animal.nascimento)
            
            user_values = {'name': especie, 'name1': linhagem, 'name2': sexo, 'name3': nascimento}

            insert_user(user_values)

            
            
    elif(option == 2):
        n = int(input('Entre com o número de aluno(s): '))
        for i in range(n):
            aluno.nome =  input('Digite o nome : ')
            aluno.vinculo_Institucional = input('Digite o vinculo_Institucional : ')
            aluno.email = input('Digite o email : ')
            aluno.telefone = input('Digite o telefone : ')
            
            nome = aluno.nome
            vinculo_Institucional = aluno.vinculo_Institucional 
            email = aluno.email
            telefone = aluno.telefone
            
            aluno(aluno.nome,aluno.vinculo_Institucional, aluno.email,aluno.telefone)
            
            user_values = {'name': nome, 'name1': vinculo_Institucional, 'name2': email, 'name3': telefone}
            
            insert_user(user_values)
        

    elif(option == 3):
        n = int(input('Entre com o número de outro(s) colaborador(es): '))
        for i in range(n):
            outros_colaboradores.nome =  input('Digite o nome : ')
            outros_colaboradores.vinculo_Institucional = input('Digite o vinculo_Institucional : ')
            outros_colaboradores.email = input('Digite o email : ')
            outros_colaboradores.telefone = input('Digite o telefone : ')

            outros_colaboradores(outros_colaboradores.nome,outros_colaboradores.vinculo_Institucional,\
                    outros_colaboradores.email,outros_colaboradores.telefone)
            
            nome = outros_colaboradores.nome
            vinculo_Institucional = outros_colaboradores.vinculo_Institucional
            email = outros_colaboradores.email
            telefone = outros_colaboradores.telefone
            
            user_values = {'name': nome, 'name1': vinculo_Institucional, 'name2': email, 'name3': telefone}
            
            insert_user(user_values)

    elif(option == 4):
        n = int(input('Entre com o número de outro(s) colaborador(es): '))
        for i in range(n):
            pesquisador.contato =  input('Digite o Contato : ')
            pesquisador.email = input('Digite o email : ')
            pesquisador.laboratorio = input('Digite o laboratorio : ')
            pesquisador.centro_de_custo = input('Digite o centro_de_custo : ')

            contato = pesquisador.contato
            email = pesquisador.email
            laboratorio = pesquisador.laboratorio
            centro_de_custo = pesquisador.centro_de_custo

            Pedro = pesquisador(pesquisador.contato,pesquisador.email, pesquisador.laboratorio,\
                pesquisador.centro_de_custo)
            
            user_values = {'name': contato, 'name1': email, 'name2': laboratorio, 'name3': centro_de_custo}
            
            insert_user(user_values)
            
        

    elif(option == 0):
        return
    
main()

connection.commit()
connection.close()
