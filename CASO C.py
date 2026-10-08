"""
INICIO
      Paso 1: Declaración de variables.
      real P. S, r
      Paso 2: Lectura o asignación de datos.
      Leer r
      Paso 3: Procesos o cálculos.
      P = 2 * 3.1416 * r
      S = 3.1416 * r * r
      Paso 4: Mostrar los resultados.
      Escribir P, S, r
FIN
"""
# Modulo: CASOC.py

r = float(input("Ingrese valor del radio: "))

P = 2 * 3.1416 * r
S = 3.1416 * r * r

print("------------------------------------")
print("PERIMETRO Y SUPERFICIE DEL CÍRCULO:")
print("------------------------------------")
print("El radio del circulo es: ", r)
print("El perimetro del circulo es: ", P)
print("La superficie del circulo es: ", S)


