import math

def raiz_cuadrada(a):
    #Devuelve la raíz cuadrada de x si es no negativo.
    if a < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return math.sqrt(a)