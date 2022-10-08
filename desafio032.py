ano = int(input("Digite um ano:"))
if ((ano % 4 == 0) and (ano % 100 != 0)) or ((ano % 4 == 0) and (ano % 100 == 0) and (ano % 400 == 0)):
    print(f"{ano} Ano é bissexto")
else:
    print(f"{ano} Ano não é bissexto")
#for para listar os anos bissextos
anoInicio = int(input("Digite o ano inicial"))
anoFinal = int(input("Digite o ano final"))
if anoInicio < anoFinal:
    for x in range(anoInicio, anoFinal, 1):
        if ((x % 4 == 0) and (x % 100 != 0)) or ((x % 4 == 0) and (x % 100 == 0) and (x % 400 == 0)):
            print(f"{x} Ano é bissexto")
        else:
            print(f"{x} Ano não é bissexto")
else:
    print("Ano de inicio deve ser menor que nao de fim")