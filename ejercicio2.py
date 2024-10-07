'''
Programa que calcule el área y el perímetro
de un rectángulo a partir de su base y su altura
Entradas:
    base: integer
    altura: integer
Salidas:
    perimetro: integer
    area: integer
Analisis:
    Se requiere calcular con las formulas para
    area y perimetro
'''
# input siempre regresa un string
# para tratarlo como otro dato se debe convertir
print("Programa que calcula área y perímetro de un rectángulo")
base = input("Escribe la base del rectángulo: ")
base = int(base)
altura = input("Escribe la altura del rectángulo: ")
altura = int(altura)
area = base * altura
perimetro = (base + altura) * 2
print("El área del rectángulo es " + str(area))
print("El perímetro del rectángulo es ", perimetro)