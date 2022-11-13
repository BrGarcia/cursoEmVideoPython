import random as rd


def gerador_lista(qtd: int, tamanho: int) -> list:
    """Gera uma lista com diversas listas randomicas"""
    lista = []
    listatemp = []
    for j in range(0, qtd):
        for r in range(0, tamanho):
            listatemp.append(rd.randint(0, 9))
        lista.append(listatemp)
        listatemp = []
    return lista


def busca_repetido(lista: list) -> list:
    """"Recebe uma lista, busca o primeiro elemento repetido
    e retorna uma lista (a,b) onde a é o elemento repetido e
    b é a posicao na lista do elemento repetido."""
    for i, numero in enumerate(lista):
        print(i, numero)
        return True


lista_lista = gerador_lista(10, 6)
for i, numero in enumerate(lista_lista):
    print(i, numero)


flag = bool(False)
for num, lista in enumerate(lista_lista):
    lista_temp = []
    lista_valores = []
    c = 0
    for i, valor in enumerate(lista):
        if flag == False:
            a = lista[i]
            for v in lista:
                if (a == v) and (c > lista.index(v)):
                    if flag == False:
                        print(f"Lista n{num} {lista}: Item Repetido: {a} - Posicao na lista: {c}")
                        print(f"")
                        print(lista)
                        flag = True
            c += 1
