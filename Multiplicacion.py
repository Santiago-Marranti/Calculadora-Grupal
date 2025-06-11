def multiplicar():
    print("Bienvenido a la calculadora de multiplicación")

    try:
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))
        
        resultado = numero1 * numero2
        print(f"El resultado de multiplicar {numero1} por {numero2} es: {resultado}")

    except ValueError:
        print("Error: Por favor ingresa valores numéricos válidos.")

# Ejecutar la función
multiplicar()