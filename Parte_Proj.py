#Cadastro dos animais, pesquisadores, salas, etc
#Quantos animais totais por laboratorio
#projeto tem limite de animais

class animal():
    def __init__(self, especie, linhagem, sexo, nascimento):
        self.especie = especie
        self.linhagem = linhagem
        self.sexo = sexo
        self.nascimento = nascimento

class aluno():
    def __init__(self, nome, vinculo_Institucional, email, telefone):
        self.nome = nome
        self.vinculo_Institucional = vinculo_Institucional
        self.email = email
        self.telefone = telefone


class outros_colaboradores():
    def __init__(self, nome, vinculo_Institucional, email, telefone):
        self.nome = nome
        self.vinculo_Institucional = vinculo_Institucional
        self.email = email
        self.telefone = telefone



class pesquisador():
    def __init__(self, Contato, email, laboratorio, centro_de_custo):
        self.Contato = Contato
        self.email = email
        self.laboratorio = laboratorio
        self.centro_de_custo = centro_de_custo


especie =  input()
linhagem = input()
sexo = input()
nascimento = input()

Camundongo = animal(especie,linhagem, sexo,nascimento)

nome =  input()
vinculo_Institucional = input()
email = input()
telefone = input()

Pedro = aluno(nome,vinculo_Institucional, email,telefone)


nome =  input()
vinculo_Institucional = input()
email = input()
telefone = input()

Pedro = outros_colaboradores(nome,vinculo_Institucional, email,telefone)


Contato =  input()
email = input()
laboratorio = input()
centro_de_custo = input()

Pedro = pesquisador(Contato,email, laboratorio,centro_de_custo)
