def sumar_numeros():
    try:
        num1 = input("Ingrese el primer número: ").replace(",", ".")
        num2 = input("Ingrese el segundo número: ").replace(",", ".")

        # Validar que ambos campos no estén vacíos
        if not num1 or not num2:
            raise ValueError("Debe ingresar dos números válidos.")

        # Convertir a float para admitir enteros y decimales
        num1 = float(num1)
        num2 = float(num2)

        resultado = num1 + num2
        print(f"El resultado de {num1} + {num2} es: {resultado}")

    except ValueError as e:
        print(f"Error: {e}")

# Llamar a la función
sumar_numeros()
