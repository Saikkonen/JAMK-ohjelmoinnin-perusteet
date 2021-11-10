eka = input("Anna kokonaisluku: ")
toka = input("Anna toinen kokonaisluku: ")
kolmas = input("Anna kolmas kokonaisluku: ")
if(eka>toka and eka>kolmas):
    print("Suurin:", eka)
elif (toka>kolmas):
    print("Suurin:", toka)
else:
    print("Suurin:", kolmas)