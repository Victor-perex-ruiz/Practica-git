otra = "si".strip().lower()

while otra == "si":
    print("****Bienvenido A la Calculadora Portátil XD*****\n")
    print("**Seleccione qué operación deseas realizar con los números respectivos**")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Exponente")
    print("")

    operacion = int(input("Ingresa el número de la operación que deseas realizar: "))
    
    # Diccionario de operaciones
    nom = {
        1: "Suma",
        2: "Resta",
        3: "Multiplicación",
        4: "División",
        5: "Exponente"
    }

    # Verificación si la operación es válida
    if operacion not in nom:
        print("Operación no válida.")
        break

    print("\nINGRESE 2 NÚMEROS:")
    try:
        a = int(input("Número 1: "))
        b = int(input("Número 2: "))

        def Calcular(a, b, operacion):
            if operacion == 1:
                return a + b
            elif operacion == 2:
                return a - b
            elif operacion == 3:
                return a * b
            elif operacion == 4:
                if b == 0:  # Manejo de división por cero
                    return "Error: No se puede dividir por cero"
                return a / b
            elif operacion == 5:
                return a ** b

        respuesta = Calcular(a, b, operacion)
        nombre = nom[operacion]
        
        print(f"\nEl RESULTADO de la {nombre} es: {respuesta}\n")
        
    except ValueError:
        print("Por favor, ingresa números válidos.")
    
    print("Si deseas continuar, escribe SI/No")
    otra = input("").strip().lower()

    if otra != "si":
        print("¡Gracias por usar la calculadora!")
        break


