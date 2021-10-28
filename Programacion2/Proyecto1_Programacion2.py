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


def pi_funcion(i):  # funcion de la ecuacion
    numerador = 4 * ((-1)**i)
    denominador = (2*i) + 1
    return numerador / denominador


terminos = int(input("Ingrese la cantidad de terminos que desea caluclar: "))

lista_terminos = range(0, terminos)

lista_resultados = list(map(pi_funcion, lista_terminos))


from functools import reduce

resultado_final = reduce(lambda a, b: a+b, lista_resultados)
print("El resultado final es:", resultado_final)


'''
RECUSIVIDAD 

Ejercicio 1 - Codificar un numero entero de la siguiente manera:
- Cada digito par sustituirlo por 1
- Cada digito impar sustituirlo por 2
Puede pasar el numero a otras representaciones para resolver el ejercicio
'''


num = 436225
num = str(num)


def codificar(Z):
    if len(Z) == 0:
        return ""
    else:
        if int(Z[0]) % 2 == 0:
            return "1" + codificar(Z[1:])
        else:
            return "2" + codificar(Z[1:])


print(codificar(num))

'''
Ejercicio 3 - Decidir si dos listas de numeros enteros son iguales


Caso Base = comparar el primer elemento de cada lista y si son iguales, comparar el resto de las listas.
'''


def verifiacar_listas(lista1, lista2):
    if len(lista1) == 1 and len(lista2) == 1:
        return lista1[0] == lista2[0]
    else:
        if len(lista1) != len(lista2):
            return False
        else:
            return (lista1[0] == lista2[0]) and (verifiacar_listas(lista1[1:], lista2[1:]))


lista_1 = [2, 3, 4, 6]
lista_2 = [2, 3, 4, 6]

print(verifiacar_listas(lista_1, lista_2))


'''
Ejercicio 4 - Realizar la division entera entre dos numeros enteros positivos A y B, (B != 0).

'''

A = 145
B = 5


def division_entera(A, B):
    if A < B:
        return 0
    else:
        return 1 + division_entera(A-B, B)


print(division_entera(A, B))
