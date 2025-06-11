import math
print ("Esta es la funcion de la raiz cuadrada")
def raiz_cuadrada(x):
    """Devuelve la raíz cuadrada de x si es no negativo."""
    if x < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return math.sqrt(x)