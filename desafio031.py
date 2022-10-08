distancia = int(input("Qual a distancia da viagem: "))
if distancia <= 200:
    valor = float(distancia) * 0.5
    print(valor)
else:
    valor = float(distancia) * 0.45
    print(valor)