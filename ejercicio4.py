'''
Ejercicio 4:
    Programa que lea 2 números y realice la suma, resta, multiplicación y división
Entradas:
    num1: int
    num2: int
Salidas:
    suma: int
    resta: int
    multiplicacion: int
    division: float
'''
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print("La suma de", num1, "+", num2, "es", suma)
print("La resta de", num1, "-", num2, "es", resta)
print("La multiplicación de", num1, "*", num2, "es", multiplicacion)
print("La división de", num1, "/", num2, "es", division)