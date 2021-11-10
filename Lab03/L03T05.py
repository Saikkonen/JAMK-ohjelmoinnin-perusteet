summa = 0
for i in range(5):
    kys = "Anna " + str(i+1) + ". luku: "
    luku = int(input(kys))
    if luku > 0:
        summa = summa + luku
print("Lukujen summa on:", summa)