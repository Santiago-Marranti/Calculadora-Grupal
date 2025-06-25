def dividir(numerador, denominador):
    try:
        resultado = numerador / denominador
        return f"Resultado: {resultado}"
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero"
