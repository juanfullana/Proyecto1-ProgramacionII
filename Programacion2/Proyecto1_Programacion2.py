""" 
Expresiones Regulares.

Ejercicio 1:

Implemente una expresión regular para validar matrículas argentinas.

Ej matrículas válidas:

LV-QWE
LQ-ABE
LV-X443
LV-S586
LV-SX334

Ejemplos matrículas inválidas:

LA-123
LX-ABC
LV
LV-344
LV-SX33UIO4
LV-SX334UIO

SOLUCION = (L(V|Q)-[A-Z]{3})|(LV-(X|S|SX)[\d]{3}$) [Si encontras una mejor, cambiala]


2. Diseñe una ER para validar cadenas de números naturales menores a 1900


Numeros validos:

120
589
899
925
1503
1900
1899

Numeros Invalidos:

3555
8888
256.24
0

SOLUCION = ^[1][0-8]?[0-9]?[0-9]?$|^[1-9][0-9]?[0-9]?$|1900 [Si encontras una mejor, cambiala]

"""
