import loguins
import menu
import gerar_filmes
from exibir_lista import *
from validacao import *


usuarios = {'1234': ['cris', 1, '123456'], '1235': ['cristi', 2, '123456']}
filmes = [{'nome': 'gato de botas 1', 'genero': 'M', 'sinopse': 'aventuras', 'capacidade': 4, 'valor': 2},
          {'nome': 'motoqueiro fantasma', 'genero': 'M', 'sinopse': 'motos', 'capacidade': 4, 'valor': 2},
          {'nome': 'bruxa', 'genero': 'M', 'sinopse': 'feticeira', 'capacidade': 4, 'valor': 2},
          {'nome': 'balei azul', 'genero': 'M', 'sinopse': 'oceano', 'capacidade': 4, 'valor': 2}
          ]
filmes_vendidos = []
opmenu_pr = 99

while (opmenu_pr != '0'):

    menu.menu_principal()
    opmenu_pr = input('\ndigite a opcao desejada = ')

    if (opmenu_pr == '1'):
        login = input('digite seu login = ')
        senha = input('digite sua senha = ')

        # ADM
        logado = loguins.fazer_login(login, senha, usuarios, 2)

        if (logado):
            print('Seja bem vindo(a)')
            while (True):
                menu.menu_adm()

                opadm = input('digite a opcao desejada = ')
                if (opadm == '1'):

                    filmes.append(gerar_filmes.gerar_filme())
                    print('\nfilme adicionado com sucesso')

                elif (opadm == '2'):
                    exibir_lista_com_busca(filmes)
                elif (opadm == '3'):
                    exibir_lista_com_busca(filmes)
                    cod_filme = int(input('digite o codigo do filme para atualizar = '))

                    filmes[cod_filme] = gerar_filmes.gerar_filme()
                    print('\nfilme atualizado com sucesso')


                elif (opadm == '4'):
                    exibir_lista_com_busca(filmes)
                    cod_filme = int(input('digite o codigo do filme para atualizar = '))
                    filmes.pop(cod_filme)
                    print('\nfilme removido com sucesso')

                elif (opadm == '5'):
                    print('-----Filmes vendidos ---')
                    for filme_vendido in filmes_vendidos:
                        print(f'Nome = {filme_vendido["nome"]}\n - Quantidade de Ingressos = {filme_vendido["quantidade_ingressos"]}')



                elif (opadm == '6'):
                    nome_filme = input('qual filme vocer quer buscar = ')
                    for filme_vendido in filmes_vendidos:
                        if filme_vendido['nome'].lower() in nome_filme.lower():
                            print(f'Filme encontrado: {filme_vendido['nome']}, Quantidade de Ingressos: {filme_vendido['quantidade_ingressos']}')

                        else:
                            print('filme não em contrado')
                elif (opadm == '7'):
                    break


                else:
                    print('opção invalida')
        else:
            print('Senha ou loguin inválido')

    elif (opmenu_pr == '2'):
        login = input('digite seu login = ')
        senha = input('digite sua senha =')

        # cliente
        logado = loguins.fazer_login(login, senha, usuarios, 1)

        if (logado):
            print('Sejá bem vindo (a) ')
            while (True):
                menu.menu_cliente()
                op_menu_cliente = input(' Digite uma opção por favor =')
                if (op_menu_cliente == '1'):
                    lista_filmes(filmes)

                elif (op_menu_cliente == '2'):
                    exibir_lista_com_busca(filmes)

                elif (op_menu_cliente == '3'):
                    filmes_vendidos = compra_filme(filmes, filmes_vendidos)

                elif(op_menu_cliente == '4'):
                    with open('filmes_vendidos.txt','r') as arquivo :
                        linhas = arquivo.readlines()

                        # Exiba as linhas do arquivo
                    for linha in linhas:
                        print(linha.strip())



                elif (op_menu_cliente == '5'):
                    break
                else:
                    print('opção invalida')


        else:
            print('Senha ou loguin inválido')

    elif (opmenu_pr == '3'):
        cadastra_usuario(usuarios)

    elif (opmenu_pr == '0'):
        print('pograma encerrando com sucesso')
    else:
        print('Opção invalida')
