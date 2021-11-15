import datetime

def showtime(sekunnit):
    paivat=int(sekunnit/(3600*24))
    sekunnit-=paivat*(3600*24)
    tunnit=int(sekunnit/3600)
    sekunnit-=3600*tunnit
    minuutit=int(sekunnit/60)
    sekunnit-=60*minuutit
    ret="%.2d:%.2d:%.2d" % (tunnit+24*paivat, minuutit, sekunnit)
    return ret

print(showtime(500))
print(showtime(10000))
print(showtime(121000))