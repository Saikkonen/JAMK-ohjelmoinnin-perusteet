class cat(object):
    def __init__(self, name="",color=""):
        self.name=name
        self.color=color

    def miau(self):
        return"Meoooooow!"

    def __str__(self):
        return self.name+ ", color: "+ self.color 

k1 = cat()
k1.name="Kit"
k1.color="black"
k2=cat("Kat", "white")

print(k1)
print(k2)
print("Kit says:", k1.miau())
print("Kat says:", k2.miau())