etunimi = input("Anna etunimi: ")
sukunimi = input("Anna sukunimi: ") [::-1]
pituus = len(etunimi)
X=etunimi[0].upper()
for i in range (0, pituus):
    print(X, end='')
print(" " + sukunimi)