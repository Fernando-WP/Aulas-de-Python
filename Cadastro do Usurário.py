import os

cadastro = []

def menu_de_opções():
    print('''===== Menu de Cadastro =====
[ 1 ] - Cadastrar uma pessoa
[ 2 ] - Ver lista de cadastro
[ 3 ] - Sair''')
    
sair = 'S'

while sair in 'S':

    menu_de_opções()
    escolhar = int(input('\nEscolhar uma das opções a cima: '))

    if escolhar == 1:
        nome = str(input('\nNome: ')).strip
        idade = int(input('Idade: '))
        gênero = str(input('Gênero: '))
        e_mail = str(input('E-mail: '))
        telefone = int(input('Telefone: '))
        cidade = str(input('Cidade: '))

        pessoa = {
        'Nome': nome,
        'Idade': idade,
        'Gênero': gênero,
        'E-mail': e_mail,
        'Telefone': telefone,
        'Cidade': cidade}
        
        cadastro.append(pessoa)
        print('\nCadastro realizado com sucesso!\n')

    elif escolhar == 2:
        for total_de_pessoa_cadastrada in enumerate(cadastro, 1):
            os.system('Cls')
            print(f'''\n
            Nome: {pessoa['Nome']}
            Idade: {pessoa['Idade']}
            Gênero: {pessoa['Gênero']}
            E-mail: {pessoa['E-mail']}
            Telefone: {pessoa['Telefone']}
            Cidade: {pessoa['Cidade']}\n''')

    elif escolhar == 3:
        os.system('cls')
        sair = str(input('Deseja continuar? [S/N]: ')).upper()
        print('\nSaindo do Programa.\n')

    else:
        print('Opção Inválida. TENTA NOVAMENTE!')