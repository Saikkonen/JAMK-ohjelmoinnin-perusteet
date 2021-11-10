from datetime import datetime

import datetime

nimi = input("Anna etunimesi: ")
syntymävuosi = int(input("Anna syntymävuotesi: "))
tämävuosi = datetime.date.today().year
vuosi = tämävuosi-syntymävuosi
print("Hei", nimi+",", "olet", vuosi, "vuotta.")
