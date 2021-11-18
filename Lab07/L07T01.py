class pelikortti(object):
    maa = "Pata","Hertta","Ruutu","Risti"
    arvo = "2-14"
    def __str__(self):
        return self.maa + " " + self.arvo
    def __init__(self, maa = "", arvo = ""):
        self.maa = maa
        self.arvo = arvo

kortti1 = pelikortti("Pata","7")
kortti2 = pelikortti("Hertta","2")
kortti3 = pelikortti("Ruutu","13")
kortti4 = pelikortti("Pata","10")
kortti5 = pelikortti("Risti","5")

print(kortti1.maa , kortti1.arvo)
print(kortti2.maa , kortti2.arvo)
print(kortti3.maa , kortti3.arvo)
print(kortti4.maa , kortti4.arvo)
print(kortti5.maa , kortti5.arvo)