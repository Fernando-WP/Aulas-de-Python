n1 = float(input('Digitar a primeira nota do aluno: '))
n2 = float(input('Digitar a segunda nota do aluno: '))

m = (n1 + n2) / 2

print(f'O aluno ficou com a média de {m:.1f}')

if m < 5.0:
    print('O aluno está REPROVADO!')
elif m <= 6.9: 
    print('O aluno está em RECUPERAÇÃO!')
elif m >= 7.0:
    print('O aluno está APROVADO!')
