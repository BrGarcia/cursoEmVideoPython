import random

for _ in range(d):
    if bool(random.getrandbits(1)):
        b.rank += 1
    else:
        b.rank -= 1
for _ in range (qtd_bolinhas):
    i = 0
    for _ in range(15):
        if bool(random.getrandbits(1)):
            i += 1
        else:
            i -= 1

    rank[i] += 1
    rank = 8
print(rank)


"""class Bolinha:
    def __init__(self):
        self.rank = 8
def tabuleiro_galton(b: Bolinha, d: int):
    for _ in range(d):
        if bool(random.getrandbits(1)):
            b.rank += 1
        else:
            b.rank -= 1
    return b.rank
qtd_bolinhas = int(input("Digite o numero de bolinhas: "))
b1 = Bolinha()
rank = [0] * 15
print(rank)
for _ in range (qtd_bolinhas):
    i = tabuleiro_galton(b1, 15)
    rank[i] += 1
    b1.rank = 8
print(rank)
"""