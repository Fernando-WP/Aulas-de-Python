print('~-' * 20)
n1 = int(input('Digita quantas vazes você quer multiplica: '))
n2 = int(input('\nDigita o número que você quer multiplica: '))
print('~-' * 20)

tx = 'TABUADA'
print(f'{tx:^20}')

print('=-' * 10)
for c in range(1, n1+1):
    t = n2 * c
    print(f'{n2} X {c} = {t}')
print('=-' * 10)