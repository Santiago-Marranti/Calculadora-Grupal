def dividir(numerador, denominador):
    try:
        resultado = numerador / denominador
        return f"Resultado: {resultado}"
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero"

# Ejemplos de uso:
print(dividir(10, 2))   # Resultado: 5.0
print(dividir(5, 0))    # Error: No se puede dividir por cero
print(dividir(7.5, 2.5)) # Resultado: 3.0