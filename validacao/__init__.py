
def validar_capacidade(texto):
    campo = int(input(texto))
    while (campo == None):
        campo = int(input(texto))
    return campo


def validar_valor(texto):
    campo = float(input(texto))
    while (campo >=4):
        campo = float(input(texto))
    return campo


def validar_campo(texto):
    campo = input(texto)
    while (len(campo) < 0):
        campo = input(texto)
    return campo
#------------------------------------------
def validar_nome(texto):
    while True:
        nome = input(texto)
        if len(nome) >= 4 and nome.isalpha():
            return nome
        else:
            print("Erro: O nome deve ter pelo menos 4 caracteres e não conter numero.")

def validar_senha(texto):
    while True:
        senha = input(texto)
        if len(senha) >= 6:
            return senha
        else:
            print("Erro: A senha deve ter pelo menos 6 caracteres.")

def validar_login(texto):
    while True:
        login = input(texto)
        if len(login) >= 4:
            return login
        else:
            print("Erro: O login deve ter pelo menos 4 caracteres.")

def validar_perfil(texto):
    while True:
        perfil = int(input(texto))
        if perfil == 1 or perfil == 2:
            return perfil
        else:
            print("Erro: Use 1 para cliente ou 2 para administrador.")

def cadastra_usuario(dicionario):
    nome = validar_nome("Digite seu nome: ")
    login = validar_login("Digite seu login: ")
    senha = validar_senha("Digite sua senha: ")
    perfil = validar_perfil("Digite seu perfil (1 para cliente, 2 para adm): ")
    dicionario[login] = [nome, perfil, senha]
    print('Cadastro realizado com sucesso!!!\n')

