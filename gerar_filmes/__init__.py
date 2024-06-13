from validacao import *
def gerar_filme():
    nome =validar_campo('digite o nome do filme = ')
    gen = validar_campo('digite o genero = ')
    sinopse = validar_campo('digite a sinopse do filme = ')
    capacidade = validar_capacidade('qual a capacidade = ')
    valor = validar_capacidade('digite o valor do ingresso = ')

    return {'nome': nome, 'genero': gen, 'sinopse': sinopse,
            'capacidade': capacidade, 'valor': valor}

#-----------------------

