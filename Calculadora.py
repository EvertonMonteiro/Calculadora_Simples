#calculadora em Python
def boas_vindas():
    print('=-' * 15)
    print('Bem vindo a Calculadora Python')
    print('=-' * 15)

def calcular(): #função que vai executar as operações para o usuário
        operacao = int(input('''
    Selecione a operação desejada:
    1 = Adição
    2 = Subtração
    3 = Multiplicação
    4 = Divisão
    ''')) #variável da operação

        num_1 = int(input('Informe o valor do primeiro número: ')) #variável do primeiro número
        num_2 = int(input('Informe o valor do segundo número: ')) #variável do segundo número

        if operacao == 1:
            print(f'{num_1} + {num_2} =')
            print(num_1 + num_2)

        elif operacao == 2:
            print(f'{num_1} - {num_2} =')
            print(num_1 - num_2)

        elif operacao == 3:
            print(f'{num_1} * {num_2} =')
            print(num_1 * num_2)

        elif operacao == 4:
            print(f'{num_1} / {num_2} =')
            print(num_1 / num_2)

        else:
            print('Você digitou uma opção inválida, tente novamente.')
            calcular()
            #Erro caso o usuário digite errado, chama a função mais uma vez.

def novamente(): #função que pergunta ao usuário se deseja chamar a função calcular() novamente
    tentar_novamente = input('''
Você deseja calcular novamente?
Insira S para Sim ou N para Não.
    ''')
    if tentar_novamente.upper() == 'S':
        calcular()

    elif tentar_novamente.upper() == 'N':
        print('Até a próxima!')

    else:
        print('Opção inválida!')
        novamente()
        # Erro caso o usuário digite errado, chama a função mais uma vez.
boas_vindas()
calcular()
novamente()