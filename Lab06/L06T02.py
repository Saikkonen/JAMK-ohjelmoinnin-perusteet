
def celToFah(celsius):
    x = celsius*1.8+32
    return format(x, ".1f")


def fahToCel(fahrenheit):
    y = (fahrenheit-32)/1.8
    return format(y, ".1f")


print(celToFah(10.0))
print(fahToCel(38.0))
