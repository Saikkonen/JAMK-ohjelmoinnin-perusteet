class Human:
    def __init__(self, name = "", age = ""):
        self.name=name
        self.age=age

    def __str__(self):
        return ("Nimi: ")+ self.name + ", ikä: "+ self.age

    def str(self):
        return self.__str__()

nimi1 = Human("Adam", "19")
nimi2 = Human("Eva", "18")

print(nimi1)
print(nimi2)