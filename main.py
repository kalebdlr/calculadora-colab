def calculadora():
    while True:
        mostrar_menu()  # Mostrar el menú
        try:
            opcion = int(input("Selecciona una opción (1-5): "))
            if opcion == 1:
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
                print("Resultado: ", suma(a, b))
            elif opcion == 2:
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
                print("Resultado: ", resta(a, b))
            elif opcion == 3:
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
                print("Resultado: ", multiplicacion(a, b))
            elif opcion == 4:
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
                print("Resultado: ", division(a, b))
            elif opcion == 5:
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida, intenta nuevamente.")
        except ValueError:
            print("Por favor ingresa un número válido.")