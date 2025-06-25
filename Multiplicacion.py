def multiplicar(a, b):

    try:
        numero1 = a
        numero2 = b
        
        resultado = numero1 * numero2
        return resultado;

    except ValueError:
        print("Error: Por favor ingresa valores numéricos válidos.")