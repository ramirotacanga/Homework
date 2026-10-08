"""
INICIO
      Paso 1: Declaración de variables.
      real areat, b, h
      Paso 2: Lectura o asignación de datos.
      Leer b, h
      Paso 3: Procesos o cálculos.
      areat = (b * h)/2.0
      Paso 4: Mostrar los resultados.
      Escribir b, h, areat
FIN
"""
#Modulo: CASOA.py

b = float(input("Base del Triángulo: "))
h = float(input("Altura del Triángulo: "))

areat = (b * h)/2.0

print("-------------------------------------")
print("ÁREA DEL TRIANGULO:")
print("-------------------------------------")
print("Base del Triángulo   : ",b)
print("Altura del Triagulo  : ",h)
print("Área del Triángulo   : ",areat)
