"""
INICIO
      Paso 1: Declaración de variables.
      real P, S, h, a, b, c
      Paso 2: Lectura o asignación de datos.
      Leer a, b, c
      Paso 3: Procesos o cálculos.
      P = a + b + c
      S = (a * h)/2.0
      Paso 4: Mostrar los resultados.
      Escribir P, S, h, a, b, c
FIN
"""

# Modulo: CASOH.py

a = float(input("Ingresar valor de la base: "))
b = float(input("Ingresar valor del primer lado: "))
c = float(input("Ingresar valor del segundo lado: "))
h = float(input("Ingresar valor de la altura: "))

P = a + b + c
S = (a * h)/2.0

print("------------------------------------")
print("PERIMETRO Y SUPERFICIE DEL TRIANGULO:")
print("------------------------------------")
print("Base:", a)
print("Lado 1:", b)
print("Laso 2:", c)
print("Altura:", h)
print("Perimetro:", P)
print("Superficie:", S)