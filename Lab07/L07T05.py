class Car:
    def __init__(self, brand = "", model = "", price =0.0):
        self.brand=brand
        self.model=model
        self.price=price

    def __str__(self):
        return ("Auto: ")+ self.brand + " "+ self.model + " "+str(self.price)

    def str(self):
        return self.__str__()

autot = []
autot.append(Car("Skoda", "Octavia", 3000))
autot.append(Car("Audi", "A4", 4000))
autot.append(Car("Volvo", "v70", 5000))

print(*autot, sep="\n")
print("Autojen hinta yhteensä:",sum(auto.price for auto in autot))