nimet = []

for x in range(10):
    nimet.append(input("Anna nimi: "))

lista = ", ".join(nimet)
print(lista)

nimet.reverse()
lista = ", ".join(nimet)
print(lista)
