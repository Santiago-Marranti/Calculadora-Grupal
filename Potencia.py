def calcular_potencia():
    print("=== Calculadora de Potencia ===")
    
    try:
        base = float(input("Ingresa la base: "))
        exponente = float(input("Ingresa el exponente: "))
        
        resultado = base ** exponente
        print(f"\nResultado: {base} ^ {exponente} = {resultado}")
    
    except ValueError:
        print("\nError: Debes ingresar números válidos.")
    except Exception as e:
        print(f"\nHa ocurrido un error inesperado: {e}")

# Ejecutar la función
if _name_ == "_main_":
    calcular_potencia()