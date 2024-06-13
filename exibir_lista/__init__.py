
def exibir_lista_com_busca(filmes):
    busca = input('digite o nome do filme = ')
    boolean = False
    for i in range(len(filmes)):
        if (busca in filmes[i]['nome']):
            print(f'{i} - {filmes[i]["nome"]}')
            boolean = True

            print('filme escolhido comsucerso')

    if boolean == False:
        print("filme não em contrado")

def lista_filmes (filmes):
    for lista_filmes in range(len(filmes)):
        if (filmes[lista_filmes]['nome']):
            print(f'{lista_filmes} - {filmes[lista_filmes]['nome']}')


def compra_filme(filmes,filmes_vendidos):
    busca = input('Digite o nome do filme: ').strip().lower()
    encontrado = None

    # Busca pelo filme na lista
    for filme in filmes:
        if busca in filme['nome'].strip().lower():
            encontrado = filme
            break

    if encontrado is None:
        print("Filme não encontrado")
        return

    # Mostrar detalhes do filme encontrado
    print(f'Filme escolhido: {encontrado["nome"]}')

    # Solicitar quantidade de ingressos
    while True:
        compra_input = input('Quantos ingressos você quer comprar: ')
        if not compra_input.isdigit():
            print('Por favor, insira um número válido para a quantidade de ingressos.')
            continue
        compra = int(compra_input)
        if compra <= 0:
            print('Por favor, insira um número válido maior que zero para a quantidade de ingressos.')
        elif compra > encontrado['capacidade']:
            print('Não há ingressos suficientes no estoque')
        else:
            break

    # Perguntar forma de pagamento
    while True:
        forma_pagamento = input('Qual é a forma de pagamento? (pix, boleto, cartão): ').strip().lower()
        if forma_pagamento not in ['pix', 'boleto', 'cartão']:
            print('Por favor, escolha uma forma de pagamento válida: pix, boleto ou cartão')
        else:
            break

    # Calcular e mostrar o total a pagar
    total_a_pagar = compra * encontrado['valor']
    print(f'Total a pagar: {total_a_pagar}')

    # Reduzir a capacidade disponível e confirmar a compra
    encontrado['capacidade'] -= compra

    # Perguntar se deseja finalizar a compra
    while True:
        finalizar_compra = input('Deseja finalizar a compra? (sim/não): ').strip().lower()
        if finalizar_compra == 'sim':
            print(f'Compra realizada com sucesso. Forma de pagamento: {forma_pagamento}')
            print('Tenha um bom filme')

            # Adicionar filme vendido à lista de filmes vendidos
            vendido = {'nome': encontrado['nome'], 'quantidade_ingressos': compra}
            filmes_vendidos.append(vendido)



            with open('filmes_vendidos.txt', 'a') as arquivo_vendidos:
                arquivo_vendidos.write(f"Filme: {vendido['nome']}, Quantidade de Ingressos: {compra}, Forma de Pagamento: {forma_pagamento}\n")

            return filmes_vendidos
        elif finalizar_compra == 'não':
            print('Compra cancelada.')

            # Registrar cancelamento no arquivo de compras canceladas
            with open('compras_canceladas.txt', 'a') as arquivo_canceladas:
                arquivo_canceladas.write(f"Filme: {encontrado['nome']}, Quantidade de Ingressos: {compra}\n")

            return
        else:
            print('Por favor, responda com "sim" ou "não".')