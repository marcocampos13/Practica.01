def union_vectores (vector1, vector2):
    return list(set(vector1) | set(vector2))

def interseccion_vectores (vector1, vector2):
    return list(set(vector1) | set(vector2))

vector_1 = ['1', '2', '3', '4', '5']
vector_2 = ['2', '4', '5', '6', '7']

print(vector_1)
print(vector_2)

union = union_vectores(vector_1, vector_2)
print("Unión:")
print(union)

interseccion = interseccion_vectores(vector_1, vector_2)
print("Intersección:")
print(interseccion)

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Unir vectores")
        print("2. Interseccionar vectores")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(union_vectores(vector_1, vector_2))
        elif opcion == "2":
            print(interseccion_vectores(vector_1, vector_2))
        elif opcion == "3":
            print("Saliendo del programa...")
            break
menu()