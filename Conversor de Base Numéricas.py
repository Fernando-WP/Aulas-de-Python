número = int(input('\033[34mDigite um número: '))
base = str(input('\033[34mEscolhar a base de conversão: \033[m'))

binário = bin(número).replace('0b', '')
octal = oct(número).replace('0o', '')
hexadecimal = hex(número).replace('0x', '').upper()

if base in 'Binário':
    print(f'\033[36mO número {número} convertido para Binário é igual a {binário}\033[m')
elif base in 'Octal':
    print(f'\033[36mO número {número} convertido para Octal é igual a {octal}\033[m')
elif base in 'Hexadecimal':
    print(f'\033[36mO número {número} convertido para Hexadecimal é igual a {hexadecimal}\033[m')
else:
    print('\033[1;31mBASE NÃO ENCONTRADA!\033[m')