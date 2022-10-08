# programa que leia 3 numeros e mostre qual e o maior e qual eh o menor
lista = []
for x in range(0, 3, 1):
    lista.append(int(input("Digite um numero")))
print(lista)
lista.sort()
print(f"O Menor é {lista[0]}")
print(f"O Maior é {lista[2]}")

#ver funcao min() e max() que retorna o valor de uma lista. por exemplo
# x = max(5, 10)  // o valor dde x vai ser 10