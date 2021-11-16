lista = []
while(True):
    nimi = input("Anna oppilaan nimi: ")
    if(len(nimi) == 0):
        break
    lista.append(nimi)

print("Oppilaita:", len(lista))
print(', '.join(lista))