saldo = 0

crédito = 0 

while True:

    print('''=======Caixa Eletrônico========
[ 1 ] - Ver Saldo
[ 2 ] - Depositar
[ 3 ] - Sacar Saldo
[ 4 ] - Ver crédito
[ 5 ] - Sair''')
    print('=' * 31)

    opção = int(input('Escolha uma das opções de cima: '))

    print('~-' * 30)
    if opção == 1:
        print(f'Seu saldo atual: R${saldo:.2f}')

    elif opção == 2:
        Valor_de_deposito = float(input('Quanto você quer depositar na sua conta? R$'))
        saldo += Valor_de_deposito
        print(f'Você depositou R${Valor_de_deposito:.2f}.')

    elif opção == 3:
        Valor_de_saque = float(input('Quanto você quer sacar da sua conta? R$'))
        saldo -= Valor_de_saque
        print(f'Você sacou R${Valor_de_saque:.2f}.')

        if saldo < 0:
            crédito_de_saque = str(input('Saldo Insuficiente. Você quer sacar em crédito? (sim/não): '))

            if crédito_de_saque in 'sim':
                diferente = Valor_de_saque - saldo
                crédito += diferente
                print(f'Você está usando R${diferente:.2f} de crédito.')
                saldo = 0
                print(f'Seu saldo: R${saldo:.2f}')

    elif opção == 4:
        print(f'Seu saldo de crédito atual: R${crédito:.2f}')

    elif opção == 5:
        print('Saindo... Tenha um ótimo dia.')
        break

    else:
        print('Opção Inválida. TENTA NOVAMENTE!')
    print('~-' * 30)