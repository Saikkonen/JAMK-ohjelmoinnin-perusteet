def get_cost(kilometrit,kulutus,hinta):
    vastaus = round(((kilometrit*kulutus)/100)*hinta, 2)
    x = format(vastaus, ".2f")
    print(x+"€")

get_cost(100,7.5,1.88)
get_cost(220,6.9,1.88)