import math
import turtle

triangulo = []
for x in range(0, 3, 1):
    triangulo.insert(x, int(input("Digite lado lado do triangulo: ")))
triangulo.sort()
# colocar os valores dos lados em variaveis simples de ler (a b c)
a = triangulo[2]
b = triangulo[1]
c = triangulo[0]
# descibri o valor dos angulos em RAD
A = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
B = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
C = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
AA = math.degrees(math.acos(A))
BB = math.degrees(math.acos(B))
CC = math.degrees(math.acos(C))
aa = a * 50
bb = b * 50
cc = c * 50
# Converter os angulos para graus e inseri-los em uma lista
listaAngulos = (math.degrees(math.acos(A)),
                math.degrees(math.acos(B)),
                math.degrees(math.acos(C)))
if a > (b + c):
    print("Não é triangulo")
else:
    print("É Triangulo")
    print(listaAngulos)
    print(sum(listaAngulos))

# desenahr o triangulo utilizando a biblioteca turtle
wn = turtle.Screen()
tri = turtle.Turtle()
def triangle(x, y):
    tri.penup()
    tri.goto(x, y)
    tri.pendown()

    tri.forward(bb)
    tri.left(180 - CC)
    tri.forward(aa)
    tri.left(180 - BB)
    tri.forward(cc)
turtle.onscreenclick(triangle, 1)
turtle.listen()
turtle.done()
