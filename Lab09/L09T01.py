filename = "nimet.txt"
try:
    file = open(filename, "w")

    while(True):
        nimi = input("Anna sukunimi: ")
        if(len(nimi) == 0):
            break
        file.write(nimi)
        file.write("\n")
except:
    print("Virhe avattaessa tiedostoa:", filename)

file.close()