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

# 🧾 Ejemplos de uso:
print("ln(10):", calcular_ln(10))       # ➝ 2.302585
print("ln(1):", calcular_ln(1))         # ➝ 0.0
print("ln(0):", calcular_ln(0))         # ➝ Error
print("ln(-5):", calcular_ln(-5))       # ➝ Error
print("ln('abc'):", calcular_ln("abc")) # ➝ Error
print("ln(1000):", calcular_ln(1000))   # ➝ 6.907755
