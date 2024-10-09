
a = float(input("Digite del valor A:"))
b = float(input("Digite del valor B:"))
c = float(input("Digite del valor C:"))

print("Resolveremos primero el numerador")
b_alcuadrado = b * 2
print(f"Resultado de B*2 es: {b_alcuadrado}")
c_portres = c * 3
print(f"Resultado de C*3 es : {c_portres}")
print("El numerador quedaría así:")
numerador = b_alcuadrado + c_portres
print(f"El resultado del denominador es:{numerador}")

print("----------------------------------------------------")

print("Ahora vamos con el denominador, resolvamos...")
if c == 0:
    print("Vuelva a comenzar el programa. El valor C no puede ser divisible por 0. Gracias")
else:
    print("Resultado de A - 2")
    a_menos2 = a - 2
    print(a_menos2)
    print("Ahora lo dividimos por C")
    denominador = a_menos2 / c

    print(f"El resultado del denominador es: {denominador}")

