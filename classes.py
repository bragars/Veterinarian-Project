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
    def __init__(self, Contato, email, laboratorio, centro_de_custo):
        self.Contato = Contato
        self.email = email
        self.laboratorio = laboratorio
        self.centro_de_custo = centro_de_custo