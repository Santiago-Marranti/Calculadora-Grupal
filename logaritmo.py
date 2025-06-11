import math

def calcular_logaritmo_base10(numero):
    if numero <= 0:
        return "Error: el logaritmo base 10 solo está definido para números mayores que cero."
    else:
        return math.log10(numero)

# Ejemplos de uso:
print(calcular_logaritmo_base10(100))   # Devuelve 2.0
print(calcular_logaritmo_base10(-5))    # Devuelve mensaje de error
print(calcular_logaritmo_base10(0))     # Devuelve mensaje de error