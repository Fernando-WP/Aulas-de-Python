from datetime import date

print('=' * 75)

ano_de_nascimento = int(input('Digitar seu ano de nascimento para saber quando deve se alistar: '))
gênero = str(input('Digitar seu gênero: '))

ano_atual = date.today().year

idade = ano_atual - ano_de_nascimento

ano_alistamento = ano_de_nascimento + 18

if idade < 18 and gênero in 'Homem':
    falta = 18 - idade
    print(f'Você ainda não completou 18 anos, seu alistameto será em {ano_alistamento}.')
    print(f'Faltam {falta} anos para você se alistar.')
elif idade == 18 and gênero in 'Homem':
    print('Você já pode se alistar IMEDIATAMENTE!')
elif gênero in 'Homem':
    falta = idade - 18
    print(f'Você ultrapassou a idade certa para se alistar, seu alistamento foi em {ano_alistamento}.')
    print(f'Já passaram {falta} anos desde o prazo do alistamento militar.')
else:
    print('Mulheres não são obrigatório se alistar no Exército Brasileiro.')

print('=' * 75)
