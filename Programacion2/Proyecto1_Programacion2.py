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

SOLUCION = (L(V|Q)-[A-Z]{3})|(LV-(X|S|SX)[\d]{3}$)z [Si encontras una mejor, cambiala]


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


'''

# Colecciones:
# Explicar en pocas palabras y utilizando diagarmas las operaciones de map, filter y reducce.
# Proponga ejemplos de cada uno (conceptuales no necesariamente en código)

----------

La funcion map() aplica una funcion a un objeto iterable (lista, tupla, etc).
Retorna un un objeto iterable que puede ser convertido con funciones como list()

***** --> map(sumar, asteriscos) --> +++++

----------

La funcion filter() aplica una funcion logica (true o false) a una secuencia de elementos.
Retorna un objeto iterable ya filtrado dependiendo si cumple la condicion logica.

*, +, *, *, -, /, *, + --> filter(asteriscos, simbolos) --> *, *, *, *

----------

La funcion reduce() aplica una funcion a los primeros dos elementos de una secuencia
y ese primer resultado lo aplica al primero de los demas elementos y asi sucesivamente
hasta retornar un unico resultado.

5, 4, 3, 2, 1 --> reduce(cual_es_mayor, numeros)
5>4?, 3, 2, 1 
5>3?, 2, 1
5>2?, 1
5>1?
5!
'''

'''
Ejercicio 2 - Calcular el numero irracional "pi" sin usar estructuras repetitivas.
'''

N = int(input("Ingrese la cantidad de terminos que desea caluclar: "))
lista_N = list()


def generar_terminos(numeros):  # Cantidad de veces a calcular
    i = 1
    while i <= numeros:
        lista_N.append(i)
        i = i + 1
    return lista_N


def pi_funcion(i):  # funcion de la ecuacion
    numerador = 4 * ((-1)**i)
    denominador = (2*i) + 1
    funcion = numerador / denominador
    return funcion


lista_N = generar_terminos(N)
print("Esta es la lista_N", lista_N)

# La lista_N contiene los valores de i
# aplico la funcion de la ecuacion a cada valor de i
lista_resultados = list(map(pi_funcion, lista_N))
print("Resultado de funciones:", lista_resultados)

# Sumo todos los valores para, supuestamente, obtener pi.
from functools import reduce
resultado_final = reduce(lambda a, b: a+b, lista_resultados)
print("El resultado final es:", resultado_final)

# Esta re verde esto pero lo charlamos si hay algo que no se entendió
# o si la logica que aplique no es la correcta