lista = []

for i in range(5):
    lista.append(int(input("Hypyn pisteet: ")))

summa = sum(lista)
x = summa-min(lista)-max(lista)
print("Pisteet yhteensä: ", x)
