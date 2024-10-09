def promedio (nota1, nota2, nota3):
    resultado = nota1 + nota2 + nota3
    resultado = resultado / 3
    return resultado

 #--------------------------------------

eleccion = input("Desea realizar un promediaje de sus últimas notas en el colegio\n1.Sí\n2.No\n1")
if eleccion > "2" and eleccion < "1":
    print("Ok, estamos procesando tu petición""Opción no válida, intentelo más tarde")
else:
    print("Ok, estamos procesando tu petición")
if eleccion == "1":
    not1 = float(input("Digite su primer nota del cuatrimestre:"))
    not2 = float(input("Digite su segunda nota del cuatrimestre:"))
    not3 = float(input("Digite su tercer nota del cuatrimestre:"))
    promedio_final = promedio (not1, not2, not3)
    print(f"Su promedio final es: {promedio_final}")
else:
    print("Ok, váyase a la fuente de la Hispanidad. Gracias ;)")
