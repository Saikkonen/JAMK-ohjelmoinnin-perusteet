lista = []
while(True):
    luku = input("Anna luku: ")
    if(len(luku) == 0):
        break
    lista.append(int(luku))

print("Alkioiden lukumäärä:", len(lista))
print("Alkioiden summa:",sum(lista))