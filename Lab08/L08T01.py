nimet = []

for x in range(10):
    nimet.append(input("Anna nimi: "))

lista = ", ".join(nimet)
print(lista)

nimet.reverse() #vaihtaa listan nimet järjestyksen käänteiseksi
lista = ", ".join(nimet)
print(lista)
