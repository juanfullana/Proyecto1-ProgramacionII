import time
import xml.etree.ElementTree as ET
from functools import reduce

print("Bienvenidos a nuestro primer proyecto!")
time.sleep(2)
print("Esperamos que sea de su agrado.")
time.sleep(2)
print("A continuación podrá disfrutar de nuestro menú interactivo.")
time.sleep(2)
print("Contamos con 4 ejercicios y sus respectivos incisos.")
time.sleep(2)

opcion_ejercicio= None
while opcion_ejercicio != "0": 
    print("[1] El primer ejercicio cuenta con 2 incisos y está destinado al uso de expresiones regulares.")
    print("[2] El segundo ejercicio cuenta con 4 incisos y está destinado al uso de funciones recursivas")
    print("[3] El tercer ejercicio cuenta con 2 incisos y está destinado al uso de colecciones")
    print("[4] El cuarto y ultimo ejercicio cuenta con 2 incisos y está destinado al intercambio de datos")
    print("[0] Exit")
    
    opcion_ejercicio = input("Ingrese el número de ejercicio al cual quiere acceder: ")
    ejercicio1 = """

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

        SOLUCION = (L(V|Q)-[A-Z]{3})|(LV-(X|S|SX)[\d]{3}$)z 

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

        SOLUCION = ^[1][0-8]?[0-9]?[0-9]?$|^[1-9][0-9]?[0-9]?$|1900

        """
    if opcion_ejercicio == "1": 
        print(ejercicio1)

    elif opcion_ejercicio == "2":

        enunciado_recursividad_1='''
            RECUSIVIDAD 

            Ejercicio 1 - Codificar un numero entero de la siguiente manera:
            - Cada digito par sustituirlo por 1
            - Cada digito impar sustituirlo por 2
            Puede pasar el numero a otras representaciones para resolver el ejercicio
            '''
        print(enunciado_recursividad_1)
        time.sleep(4)
        num = input("Ingrese el numero a codificar: ")
        num = str(num)


        def codificar(Z):
            if len(Z) == 0:
                return ""
            else:
                if int(Z[0]) % 2 == 0:
                    return "1" + codificar(Z[1:])
                else:
                    return "2" + codificar(Z[1:])


        print("El numero codificado es: ", (codificar(num)))
        
        time.sleep(4)

        enunciado_recursividad_2 = '''
        Convertir una lista de listas en una sola lista que tenga todos los elementos de las listas originales.
        Ejemplo: Si L = [ [1, 2, 3], [4, 5, 6], [7], [8] ] la lista resultante deberá ser L2 = [1,2,3,4,5,6,7,8]
        '''
        print(enunciado_recursividad_2)

        time.sleep(4)

        L = [[1, 2, 3], [4, 5, 6], [7], [8]]


        def union_de_listas(lista_madre):
            if len(lista_madre) == 1:
                return lista_madre[0]
            else:
                lista_resultado = lista_madre[0] + union_de_listas(lista_madre[1:])
                return lista_resultado


        print(union_de_listas(L))

        time.sleep(4)

        enunciado_recursividad_3='''
        Ejercicio 3 - Decidir si dos listas de numeros enteros son iguales
        
        '''
        print(enunciado_recursividad_3)
        time.sleep(4)


        def verifiacar_listas(lista1, lista2):
            if len(lista1) == 1 and len(lista2) == 1:
                return lista1[0] == lista2[0]
            else:
                if len(lista1) != len(lista2):
                    return False
                else:
                    veredicto = (lista1[0] == lista2[0]) and (verifiacar_listas(lista1[1:], lista2[1:]))
                    return veredicto


        lista_1 = []
        n = int(input("Ingrese el numero de elementos de la lista 1 : ")) 
    
        for i in range(0, n): 
            ele = [int(input("Ingrese un numero entero: "))] 
            lista_1.append(ele) 
        
        lista_2 = []
        n = int(input("Ingrese el numero de elementos de la lista 2: ")) 
    
        for i in range(0, n): 
            ele = [int(input("Ingrese un numero entero: "))] 
            lista_2.append(ele) 

        if (verifiacar_listas(lista_1, lista_2)) == True:
            print ("Ambas listas son iguales!")
        else:
            print("Las listas no son iguales!")

        enunciado_recursividad_4='''
        Ejercicio 4 - Realizar la division entera entre dos numeros enteros positivos A y B, (B != 0).

        '''
        print (enunciado_recursividad_4)
        time.sleep(3)
        A = int(input("Ingrese un numero entero positivo: "))
        B = int(input("Ingrese un numero entero positivo: "))


        def division_entera(A, B):
            if A < B:
                return 0
            else:
                return 1 + division_entera(A-B, B)


        print("El resultado de la division es: ",division_entera(A, B))
        print("")

    elif opcion_ejercicio == "3":
        enunciado_colecciones_1='''

        # Colecciones:
        # Explicar en pocas palabras y utilizando diagarmas las operaciones de map, filter y reducce.
        # Proponga ejemplos de cada uno (conceptuales no necesariamente en código)

        ----------

        La funcion map() aplica una funcion a un objeto iterable (lista, tupla, etc).
        Retorna un un objeto iterable que puede ser convertido con funciones como list()

        Ver diagrama 1.

        ----------

        La funcion filter() aplica una funcion logica (true o false) a una secuencia de elementos.
        Retorna un objeto iterable ya filtrado dependiendo si cumple la condicion logica.

        Ver diagrama 2.

        ----------

        La funcion reduce() aplica una funcion a los primeros dos elementos de una secuencia
        y ese primer resultado lo aplica al primero de los demas elementos y asi sucesivamente
        hasta retornar un unico resultado.

        Ver diagrama 3.
        '''

        enunciado_colecciones_2='''
        Ejercicio 2 - Calcular el numero irracional "pi" sin usar estructuras repetitivas.
        '''
        print (enunciado_colecciones_1)
        print("La resolucion se encuentra en el pdf adjunto en el respositorio correspondiente al proyecto")
        time.sleep(10)

        print(enunciado_colecciones_2)
        time.sleep(2)


        def pi_funcion(i):  # funcion de la ecuacion
            numerador = 4 * ((-1)**i)
            denominador = (2*i) + 1
            return numerador / denominador


        terminos = int(input("Ingrese la cantidad de terminos que desea calcular: "))

        lista_terminos = range(0, terminos)

        lista_resultados = list(map(pi_funcion, lista_terminos))

        resultado_final = reduce(lambda a, b: a+b, lista_resultados)
        print("El resultado final es: ", resultado_final)
        print("")
        time.sleep(4)

    elif opcion_ejercicio == "4":
        enunciado_intercambio_datos_1='''
        
        Ejercicio de intercambio de datos

        Se necesita diseñar un formato para intercambiar datos de estaciones meteorológicas. El sistema tiene N
        estaciones cada una con su localización (latitud y longitud) y un nombre alfanumérico. Las estaciones pueden
        tener diferentes combinaciones de sensores entre: humedad, dirección del viento, velocidad del viento,
        temperatura (que puede estar en grados celsius o fahrenheit) y presión atmosférica. No todas las estaciones
        tienen todos los sensores, pero al menos tienen uno. Los sensores deben almacenar por separado la
        magnitud leída de su unidad de medición.
        Además cada estación almacena el voltaje en milivolts de su batería una vez por segundo y el formato de
        archivo debe mantener las últimas 20 mediciones.

        1. A partir del nombre de la estación, computar la cantidad de sensores disponible y mostrar por pantalla
        los diferentes sensores, cada uno deberá mostrar el tipo y la variable medida:
        '''

        
        print(enunciado_intercambio_datos_1)
        time.sleep(10)

        with open('Sensores.xml', 'r',encoding= 'utf-8') as f:
            data = f.read()

        raiz = ET.fromstring(data)

        menor_promedio_voltajes_estaciones = None
        estacion_menor_promedio = 0

        estaciones = (raiz.find('estaciones'))
        for estacion in estaciones:
            print("Estacion: "+estacion.find('name').text)
            print("Latitud: "+estacion.find("latitud/magnitud").text + estacion.find("latitud/unidad").text)
            print("Longitud: "+estacion.find("longitud/magnitud").text + estacion.find("longitud/unidad").text)
            
            sensores = estacion.find('sensores')
            print("Cantidad de sensores: ", len(sensores))
            for sensor in sensores:
                print(sensor.get("tipo").capitalize(),": ", sensor.find("magnitud").text, sensor.find("unidad").text)
            
            voltajes = estacion.find('voltajes')
            voltajes_sum = 0
            for voltaje in voltajes:
                voltajes_sum += float(voltaje.find("magnitud").text)
            promedio_voltajes_estacion = voltajes_sum/(len(voltajes))
            
            if (menor_promedio_voltajes_estaciones == None) or (promedio_voltajes_estacion < menor_promedio_voltajes_estaciones):
                menor_promedio_voltajes_estaciones = promedio_voltajes_estacion
                estacion_menor_promedio = estacion.find('name').text
            print("")
            print("")

            
            enunciado_intercambio_datos_2 = '''
            2. Calcular cuál es la estación con menos batería, es decir, la estación con menor valor promedio de
            voltaje.
            '''
        print(enunciado_intercambio_datos_2)
        time.sleep(3)

        print("La estacion con menor batería es: ",estacion_menor_promedio,"su voltaje promedio es de: ", menor_promedio_voltajes_estaciones,"mV")
        print("")
        print("")
    
    elif opcion_ejercicio == "0":
        print("Nos vemos la proxima!")
