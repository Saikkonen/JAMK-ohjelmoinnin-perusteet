määrä = input("Anna numero väliltä 1-10: ")
lista = []
for i in range(int(määrä)):
    lista.append(str((i+1)*(i+1)))
for i in range(len(lista)):
    print("Luvun:",(str(i+1)), "neliö on",lista[i])