valor_da_casa = float(input('Digite o valor da casa: R$'))
salário = float(input('Digite o salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

a = valor_da_casa / (anos * 12)
b = salário * 30 / 100

print(f'Para compra uma casa de R${valor_da_casa:.2f} em {anos} anos, seu prestação será igual a R${a:.2f}')
if a <= b:
    print('\033[1;32mEmpréstimo APROVADO!\033[m')
else:
    print('\033[1;31mEmpréstimo NEGADO!\033[m')