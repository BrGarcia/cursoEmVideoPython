# 30    black       preto       40
# 31    red         vermelho    41
# 32    green       verde       42
# 33    yellow      amarelo     43
# 34    blue        azul        44
# 35    Magenta     Magenta     45
# 36    cyan        ciano       46
# 37    grey        Cinza       47
# 97    white       branco      107

#programa aprovar emprestimo bancario
# para comrpa de casa  qual valor da casa o salario e quantos amos ela vai pagar
valorCasa = float(0)
salarioCliente = float(0)
qtdAnos = int(0)
print('\33[97;41m BANCO BRUNO  \33[m')
print('1 - Para Fincanciamento imobiliario ')
print('2 - Para Fincanciamento estudantil ')
print('3 - Para Fincanciamento Veicular ')
menuOpc = int(input('Digite a opção: '))
if menuOpc == 1:
    print('Financiamento Imobiliario')
    valorCasa = float(input("Qual o Valor do imovel: "))
    salarioCliente = float(input("Qual a renda do cliente: "))
    qtdAnos = float(input("Quantos anos o financiamento: "))
    a = valorCasa / (qtdAnos * 12)
    b = salarioCliente * 0.3
    i = float(0.005)
    pv = valorCasa
    n = qtdAnos * 12

    if a > b:
        print("\33[31m Emprestimo não aprovado\33[m")
        print(f"Valor da Parcela mensal R${a:.2f}")
        print(f"Renda minima: R${a*100/30:.2f}")
    else:
        print('\33[32m Financiamento APROVADO \33[m')
        print(f'Valor das parcelas mensais R${a:.3f}')

    print('Calculo com juros')
    pmt = pv / (((1 + i) ** n - 1) / ((1 + i) ** (n - 1) * i))
    print(f'R$ {pmt:.2f}')
    print(pmt*12*qtdAnos)