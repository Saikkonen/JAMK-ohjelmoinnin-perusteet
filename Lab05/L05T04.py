def get_fuel(kilometrit,kulutus):
    vastaus = round((kilometrit*kulutus)/100, 1)
    print(vastaus, "ltr")
get_fuel(100,7.5)
get_fuel(220,6.9)