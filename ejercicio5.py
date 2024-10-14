'''
Ejercicio 5:
    Programa que convierte grados Fahrenheit a grados Celsius
Entradas:
    grados_f: float
Salidas
    grados_c: float
Análisis:
    Se hace la conversión utilizando la fórmula
    (0°F − 32) × 5/9
'''
grados_f = float(input('Ingresa los grados Fahrenheit: '))
grados_c = (grados_f - 32) * (5 / 9)
print(grados_f, "ºF es equivalente a", grados_c, "ºC")