"""
INICIO
      Paso 1: Declaración de variables.
      entero cod, can
      real pre, com, impdes, imppa, reg
      Paso 2: Lectura o asignación de datos.
      Leer cod, can

      Paso 3: Procesos o cálculos.
      Si cod = 1000 Entonces
            pre = 170.5
      Sino Si cod = 1001 Entonces
            pre = 190.5
      Sino Si cod = 1002 Entonces
            pre = 100.5
      Sino
            pre = 600.5
      Fin Si

      com = pre * can

      Si can < 20 Entonces
            impdes = com * 0.05
      Sino Si can < 35 Entonces
            impdes = com * 0.09
      Sino Si can < 45 Entonces
            impdes = com * 0.12
      Sino Si can < 55 Entonces
            impdes = com * 0.16
      Sino
            impdes = com * 0.20
      Fin Si
      
      imppa = com - impdes

      Si imppa > 2000 Entonces
            reg = 2
      Sino
            reg = 1
      Fin Si
      Paso 4: Mostrar los resultados.
      Escribir com, impdes, imppa, reg
FIN
"""

#Modulo: CASO2.py

cod = int(input("Ingrese el código: "))
can = int(input("Ingrese la cantidad: "))

if cod == 1000:
    pre = 170.5
elif cod == 1001:
    pre = 190.5
elif cod == 1002:
    pre = 100.5
else:
    pre = 600.5

com = pre * can

if can < 20:
    impdes = com * 0.05
elif can < 35:
    impdes = com * 0.09
elif can < 45:
    impdes = com * 0.12
elif can < 55:
    impdes = com * 0.16
else:
    impdes = com * 0.20

imppa = com - impdes

if imppa > 2000:
    reg = 2
else:
    reg = 1

print("------------------------------------")
print("BOLETA DE COMPRA:")
print("------------------------------------")
print("Importe de compra:", com)
print("Importe de descuento:", impdes)
print("Importe a pagar:", imppa)
print("Regalo:", reg, "Tablet(s)")