arvosanat = []

while(True):
    muuttuja = input("Anna arvosana: ")
    if(len(muuttuja) == 0):
        break
    arvosanat.append(muuttuja)

lista = list(map(int, arvosanat))

print("Arvosanoja:", len(arvosanat))
print("Arvosanojen keskiarvo:", sum(lista)/len(lista))