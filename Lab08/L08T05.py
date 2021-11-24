import random

lista = []

def lotto():
    for x in range(7):
        n = random.randint(1,40)
        lista.append(n)
    lista.sort()
    print(*lista, sep=", ")

lotto()