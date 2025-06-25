import math

def calcular_logaritmo_base10(numero):
    if numero <= 0:
        return "Error: el logaritmo base 10 solo está definido para números mayores que cero."
    else:
        return math.log10(numero)