"""
INICIO
      Paso 1: Declaración de variables.
      real dona, cs, pm, es, co, asi
      Paso 2: Lectura o asignación de datos.
      Leer dona
      Paso 3: Procesos o cálculos.
      cs = dona * 0.25
      es = dona * 0.35
      co = (es + cs) * 0.28
      pm  = co * 0.40 
      asi = dona - (cs + es + co + pm)
      Paso 4: Mostrar los resultados.
      Escribir dona, cs, pm, es, co, asi 
FIN
"""
#Modulo: CASO1.py

dona = float(input("Insertar monto de la donación: "))

cs = dona * 0.25
es = dona * 0.35
co = (es + cs) * 0.28
pm = co * 0.40 
asi= dona - (cs + es + co + pm)

print("------------------------------------")
print("DINERO CORRESPONDIENTE A CADA ÁREA:")
print("------------------------------------")
print("Donación total: ", dona)
print("Centro de salud: ", cs)
print("Escuela: ", es)
print("Comedor: ", co)
print("Posta médica: ", pm)
print("Asilo: ", asi)


