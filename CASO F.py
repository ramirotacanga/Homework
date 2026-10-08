"""
INICIO
      Paso 1: Declaración de variables.
      real V, r
      Paso 2: Lectura o asignación de datos.
      Leer r
      Paso 3: Procesos o cálculos.
      V = (4 / 3) * 3.1416 * R * R
      Paso 4: Mostrar los resultados.
      Escribir V, r
FIN
"""

#Modulo: CASOF.py

r = float(input("Ingrese valor del radio: "))

V = (4 / 3) * 3.1416 * r * r

print("------------------------------------")
print("VOLUMEN DE LA ESFERA:")
print("------------------------------------")
print("El radio de la esfera es: ", r)
print("El volumen de la esfera es: ", V)
