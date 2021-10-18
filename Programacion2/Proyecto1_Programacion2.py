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

SOLUCION = (L(V|Q)-[A-Z]{3})|(LV-(X|S|SX)[\d]{3}$)

Probando si anda

"""
