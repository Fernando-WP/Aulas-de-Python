print('~-' * 20)
print('''=========OPERADORES========
[ x ] - Multiplicação
[ + ] - Soma
[ - ] - Subtração
[ / ] - Divisão''')
operadores = str(input('\nEscolha um dos operadores: '))
n1 = int(input('\nDigita quantas vazes você quer multiplica: '))
n2 = int(input('\nDigita o número que você quer multiplica: '))
print('~-' * 20)

tx = 'TABUADA'
print(f'{tx:^20}')

print('=-' * 10)
for c in range(1, n1+1):
    if operadores == 'x':
        M = n2 * c
        print(f'{n2} X {c} = {M}')
    elif operadores == '+':
        M = n2 + c
        print(f'{n2} + {c} = {M}')
    elif operadores == '-':
        M = n2 - c
        print(f'{n2} - {c} = {M}')
    elif operadores == '/':
        M = n2 / c
        print(f'{n2} / {c} = {M}')
print('=-' * 10)