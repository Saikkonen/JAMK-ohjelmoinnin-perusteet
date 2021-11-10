nimi = input("Anna etunimesi ")
pituus = len(nimi)
print("Nimessä", nimi, "on", pituus, "kirjainta.")
X=nimi[0].upper()
for i in range (0, pituus):
    print(X, end='')