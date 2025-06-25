import math

def calcular_ln(valor):
    try:
        # Convertimos el valor a float por si viene como cadena
        numero = float(valor)

        if numero <= 0:
            return "Error: el argumento del logaritmo natural debe ser mayor que cero."
        
        resultado = math.log(numero)  # logaritmo natural (base e)
        return round(resultado, 6)    # redondeado a 6 decimales
    
    except ValueError:
        return "Entrada inválida: debe ingresar un número válido."
    except Exception as e:
        return f"Error inesperado: {str(e)}"