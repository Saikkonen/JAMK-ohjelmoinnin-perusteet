määrä = input("Montako lukua: ")
lista = []
for i in range(int(määrä)):
    lista.append(10*i)
for i in range(len(lista)):
    print(str(i+1)+". luku:",lista[i])