#1. Desarrolle un programa Python que reciba un número entero e indique si es un número perfecto o no.  Un número perfecto es aquel que la suma de sus divisores, exceptuando el mismo, es el mismo número, un ejemplo de esto es el 6 ya que sus divisores (1,2,3) sumados dan 6.

def numero_perfecto(numero):
    suma_divisores = 0

    for i in range (1, numero):
        if numero % i == 0:
            suma_divisores += i

    if suma_divisores == numero:
        return True
    else:
        return False

numero = int(input("Ingrese un número entero: "))

if numero_perfecto(numero):
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero} no es un número perfecto.")

print("*********************************************************")


# Desarrolle un programa en Python que permita simular la división entera de un número entre otro, no aplicar operaciones de división (% | /), al final debe imprimir el resultado y residuo de la operación.

def division_entera(dividendo, divisor):
    cociente = 0
    residuo = dividendo

    while residuo >= divisor:
        residuo -= divisor
        cociente += 1

    return cociente, residuo

dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))

if divisor == 0:
    print("El divisor no puede ser 0.")
else:
    cociente, residuo = division_entera(dividendo, divisor)

    print(f"El resultado de la división entera es: Cociente = {cociente}, Residuo = {residuo}")
    print("*********************************************************")


# 3.Utilizando una función Random en Python, cree una aplicación que permita calcular un número entero no menor a 15, pero tampoco mayor a 30, posterior a este proceso el programa debe indicar cuál número calculó y el usuario deberá llenar 4 vectores de 3 campos cada uno, con las siguientes restricciones:

import random

num_calculado = random.randint(10, 50)
print(f"El número calculado es: {num_calculado}")

vectores = []

for i in range(4):
    print(f"Llenando el vector {i + 1}:")
    vector = []
    for j in range(3):
        numero = int(input(f"Ingrese el valor {j + 1} del vector {i + 1}: "))
        vector.append(numero)
    vectores.append(vector)

for i, vector in enumerate(vectores):
    suma = sum(vector)
    print(f"La suma del vector {i + 1} es {suma}.")
    if suma != num_calculado:
        print(f"Error: La suma del vector {i + 1} no coincide con el número calculado.")

todos_numeros = []
for vector in vectores:
    todos_numeros += vector

if len(todos_numeros) != len(set(todos_numeros)):
    print("Error: Hay números repetidos entre los vectores.")
else:
    print("No hay números repetidos entre los vectores.")
print("*******************************")


# 4.Para la siguiente expresión algebraica y mediante lenguaje Python genere la impresión en pantalla de la tabla de la verdad, que usted ya conoce de cursos como fundamentos de programación y fundamento de TI.
# F = (x’ * ( y + z’)) * z
# Considere que:
# ‘ es la compuerta not
# * es la compuerta and
# + es la compuerta or

print(" x | y | z | F")
print("----------------")

for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            F = (not x and (y or not z)) and z
            print(f" {x} | {y} | {z} | {int(F)}")
print("************************************")


# 5. Desarrollar la siguiente fórmula matemática utilizando para ello lenguaje Python, considerando la declaración de variables, captura de datos, la impresión de cada subproceso, hasta la impresión final del resultado:

try:
    valor_a = float(input("Ingrese el valor de A: "))
    valor_b = float(input("Ingrese el valor de B: "))
    valor_c = float(input("Ingrese el valor de C: "))

    b_alcuadrado = valor_b ** 2
    print(f"El valor de b^2 es: {b_alcuadrado}")

    c_por_3 = valor_c * 3
    print(f"El valor de c * 3 es: {c_por_3}")

    numerador = b_alcuadrado + c_por_3
    print(f"El numerador (b^2 + c * 3) es: {numerador}")

    a_menos_2 = valor_a - 2
    print(f"El valor de (a - 2) es: {a_menos_2}")

    if valor_c == 0:
        print("Error: El valor de C no puede ser 0.")
    else:
        denominador = a_menos_2 / valor_c
        print(f"El denominador ((a - 2) / c) es: {denominador}")

        x = numerador / denominador
        print(f"El resultado final de x es: {x}")

except ValueError:
    print("Error: Por favor ingrese solo números válidos.")
print("*******************************")


# 6. 6.Desarrolle un programa en Python que permita procesar dos vectores previamente cargados, las dimensiones de estos vectores pueden ser tanto iguales como diferentes, este programa deberá de contar con dos subrutinas que calculen:
# La unión entre ambos vectores.
# La intersección entre ambos vectores.

def union_vectores(vector1, vector2):
    return list(set(vector1) | set(vector2))

def interseccion_vectores(vector1, vector2):
    return list(set(vector1) & set(vector2))

def main():
    vector_a = ['a', 'b', 'c', 'd', 'e']
    vector_b = ['a', 'e', 'i', 'o']

    print("Vector A:", vector_a)
    print("Vector B:", vector_b)

    union = union_vectores(vector_a, vector_b)
    print("\nUnión de los vectores:")
    print(union)

    interseccion = interseccion_vectores(vector_a, vector_b)
    print("\nIntersección de los vectores:")
    print(interseccion)

if __name__ == "__main__":
    main()
print("*******************************")


# 7.Desarrolle un programa en Python que permita simular el comportamiento de la siguiente gráfica:
#Parecido al problema anterior, usted defina manualmente las dos matrices de datos, con datos cargados manualmente, puede utilizar los mismos del ejemplo para validar sus salidas:
#Impresión de ambas matrices.
#Impresión de la matriz de las operaciones de suma
#Impresión de la matriz de resultados

def multiplicar_matrices(A, B):
    filas_A = len(A)
    columnas_A = len(A[0])
    columnas_B = len(B[0])

    resultado = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]

    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(columnas_A):
                resultado[i][j] += A[i][k] * B[k][j]

    return resultado

A = [
    [3, 2, 1],
    [1, 1, 3],
    [0, 2, 1]
]

B = [
    [2, 1],
    [1, 0],
    [3, 2]
]

resultado = multiplicar_matrices(A, B)

print("Resultado de la multiplicación:")
for fila in resultado:
    print(fila)
print("*******************************")


# 8.Se desea aplicar una encuesta a N cantidad de estudiantes, para determinar el consumo de frutas que realizan durante la semana y determinar el grado de alimentación saludable que la población estudiantil posee. Claro es una estadística.
# Los valores por representar son:
# 0 - Mucho
# 1 - Mediano
# 2 - Poco

import random


def crear_encuesta(num_estudiantes):
    opciones = ["Mucho", "Mediano", "Poco"]
    encuesta = []

    for _ in range(num_estudiantes):
        respuesta = random.choice(opciones)
        encuesta.append(respuesta)

    return encuesta


def mostrar_resultados(encuesta):
    print("\nResultados de la encuesta:")
    print("  1 2 3 4 5 6 7")
    for opcion in ["Mucho", "Mediano", "Poco"]:
        fila = [opcion]
        for respuesta in encuesta:
            if respuesta == opcion:
                fila.append("*")
            else:
                fila.append(" ")
        print(" ".join(fila))


def analizar_resultados(encuesta):
    mucho = encuesta.count("Mucho")
    mediano = encuesta.count("Mediano")
    poco = encuesta.count("Poco")

    print("\nAnálisis de resultados:")
    print(f"{mucho} estudiantes consumen mucha fruta")
    print(f"{mediano} estudiantes consumen medianamente frutas")
    print(f"{poco} estudiantes consumen poca fruta")

num_estudiantes = 7
resultados = crear_encuesta(num_estudiantes)

mostrar_resultados(resultados)
analizar_resultados(resultados)
print("*******************************")
