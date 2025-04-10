# Calculadora Básica

def suma(a, b):
    return a + b

# Aquí se agregarán las demás funciones:
# - resta(a, b)
# - multiplicacion(a, b)
# - division(a, b)

if __name__ == "__main__":
    while True:
        print("\n--- Calculadora Básica ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == '5':
            print("¡Hasta luego!")
            break

        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))

        if opcion == '1':
            print("Resultado:", suma(a, b))
        elif opcion == '2':
            print("Resultado: resta(a, b) # (a implementar)")
        elif opcion == '3':
            print("Resultado: multiplicacion(a, b) # (a implementar)")
        elif opcion == '4':
            print("Resultado: division(a, b) # (a implementar)")
        else:
            print("Opción inválida.")
