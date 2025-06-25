def calcular_potencia(a, b):
    print("=== Calculadora de Potencia ===")
    
    try:
        base = a
        exponente = b
        
        resultado = base ** exponente
        return resultado;
    
    except ValueError:
        print("\nError: Debes ingresar números válidos.")
    except Exception as e:
        print(f"\nHa ocurrido un error inesperado: {e}")