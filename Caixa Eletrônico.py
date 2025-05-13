Saldo = 0

Crédito = 0 

while True:

    print('''=======Caixa Eletrônico========
[ 1 ] - Ver Saldo
[ 2 ] - Depositar
[ 3 ] - Sacar Saldo
[ 4 ] - Ver crédito
[ 5 ] - Sair''')
    print('=' * 31)

    Opção = int(input('Escolha uma das opções de cima: '))

    print('~=' * 30)
    if Opção == 1:
        print(f'Seu saldo atual: R${Saldo:.2f}')

    elif Opção == 2:
        Valor_de_Deposito = float(input('Quanto você quer depositar na sua conta? R$'))
        Saldo += Valor_de_Deposito
        print(f'Você depositou R${Valor_de_Deposito:.2f}.')

    elif Opção == 3:
        Valor_de_Saque = float(input('Quanto você quer sacar da sua conta? R$'))
        Saldo -= Valor_de_Saque
        print(f'Você sacou R${Valor_de_Saque:.2f}.')

        if Saldo < 0:
            Crédito_de_Saque = str(input('Saldo Insuficiente. Você quer sacar em crédito? (sim/não): '))

            if Crédito_de_Saque in 'sim':
                Valor_de_Crédito = Valor_de_Saque - Saldo
                Crédito += Valor_de_Crédito
                print(f'Você está usando R${Valor_de_Crédito:.2f} de crédito.')
                Saldo = 0
                print(f'Seu saldo: R${Saldo:.2f}')

    elif Opção == 4:
        print(f'Seu saldo de crédito atual: R${Crédito:.2f}')

    elif Opção == 5:
        print('Saindo... Tenha um ótimo dia.')
        break

    else:
        print('Opção Inválida. TENTA NOVAMENTE!')
    print('~=' * 30)