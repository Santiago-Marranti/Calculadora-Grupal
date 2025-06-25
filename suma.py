def sumar_numeros(a, b):
    try:
        num1 = a
        num2 = b

        # Validar que ambos campos no estén vacíos
        if not num1 or not num2:
            raise ValueError("Debe ingresar dos números válidos.")

        # Convertir a float para admitir enteros y decimales
        num1 = float(num1)
        num2 = float(num2)

        resultado = num1 + num2
        return resultado;

    except ValueError as e:
        print(f"Error: {e}")
