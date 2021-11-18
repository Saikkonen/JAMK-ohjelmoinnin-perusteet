class Mobile:
    def __init__(self, brand = "", model = "", price =0.0):
        self.brand=brand
        self.model=model
        self.price=price

    def __str__(self):
        return self.brand + " " + self.model + ", " + str(self.price) + "€"

phone1 = Mobile("Samsung", "Galaxy", 349)
phone2 = Mobile("Apple", "iPhone 12", 899)

print(phone1)
print(phone2)
