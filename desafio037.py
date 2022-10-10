#leia um numero e o escreva em binanario octal e ou hexa
import math
numero = int(input("Digite um numero"))

print('1 - BINARIO')
print('2 - OCTAL')
print('3 - HEXADECIMAL')
menu = int(input("Converter para qual base? "))
if menu == 1:
    print(bin(numero))
if menu == 2:
    print(oct(numero))
if menu == 3:
    print(hex(numero))