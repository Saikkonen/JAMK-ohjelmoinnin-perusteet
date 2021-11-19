rek = []

while(True):
    muuttuja = input("Anna rekisterinumero: ")
    if(len(muuttuja) == 0):
        break
    rek.append(muuttuja)

lista = ", ".join(sorted(rek))   
print(lista)
