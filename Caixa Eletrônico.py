import os

Saldo = 0

Crédito = 0

def exibir_opções():

    print('''=======Caixa Eletrônico========
    [ 1 ] - Ver Saldo
    [ 2 ] - Depositar
    [ 3 ] - Sacar Saldo
    [ 4 ] - Ver crédito
    [ 5 ] - Sair''')
    print('=' * 31)

def opcao_invalida():
    os.system('cls')
    print('Opção Inválida. TENTA NOVAMENTE!\n')
    input('|Pressionar qualquer teclar para voltar| ')
    os.system('cls')
    main()

def saindo_do_caixa_eletrônica():
    os.system('cls')
    print('Saindo . . . Tenha um ótimo dia.\n')

def escolhar_de_opções():
    global Saldo, Crédito

    try: 
        Opcao = int(input('\nEscolha uma das opções de cima: '))

        if Opcao == 1:
            print(f'\nSeu saldo atual: R${Saldo:.2f}\n')

        elif Opcao == 2:
            Valor_de_Deposito = float(input('\nQuanto você quer depositar na sua conta? R$'))
            Saldo += Valor_de_Deposito
            print(f'\nVocê depositou R${Valor_de_Deposito:.2f}\n')

        elif Opcao == 3:
            Valor_de_Saque = float(input('\nQuanto você quer sacar da sua conta? R$'))
            Saldo -= Valor_de_Saque
            print(f'\nVocê sacou R${Valor_de_Saque:.2f}.\n')

            if Saldo < 0:
                Crédito_de_Saque = str(input('Saldo Insuficiente. Você quer sacar em crédito? (sim/não): '))

                if Crédito_de_Saque in 'sim':
                    Valor_de_Crédito = Valor_de_Saque - Saldo
                    Crédito += Valor_de_Crédito
                    print(f'\nVocê está usando R${Valor_de_Crédito:.2f} de crédito.')
                    Saldo = 0
                    print(f'\nSeu saldo: R${Saldo:.2f}\n')

        elif Opcao == 4:
            print(f'\nSeu saldo de crédito atual: R${Crédito:.2f}\n')

        elif Opcao == 5:
            saindo_do_caixa_eletrônica()
            return
                    
        else:
            opcao_invalida()
    except:
        opcao_invalida()

    main()
    
def main():
    exibir_opções()
    escolhar_de_opções()

if __name__ == '__main__':
    main()