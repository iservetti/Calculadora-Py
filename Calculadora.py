def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    else:
        return a / b

print("Calculadora")

while True:
    print("\nSelecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = int(input("Ingrese el número de la operación que desea realizar: "))

    if opcion == 1:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("El resultado es:", suma(a, b))

    elif opcion == 2:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("El resultado es:", resta(a, b))

    elif opcion == 3:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("El resultado es:", multiplicacion(a, b))

    elif opcion == 4:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("El resultado es:", division(a, b))

    elif opcion == 5:
        print("¡Muchas gracias, Ignacio!")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
