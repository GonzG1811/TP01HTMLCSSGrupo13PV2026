import os

def menu():
    print("\n--- SISTEMA DE BIBLIOTECA ---")
    print("1. Registrar préstamo")
    print("2. Ver libros prestados")
    print("3. Salir")
    return input("Seleccione una opción: ")

def registrar_prestamo():
    libro = input("Nombre del libro: ")
    persona = input("Nombre de la persona: ")
    
    with open("prestamos.txt", "a") as archivo:
        archivo.write(f"Libro: {libro} | Prestado a: {persona}\n")
    print("¡Registro guardado con éxito!")

def ver_prestamos():
    print("\n--- LISTA DE PRÉSTAMOS ---")
    if not os.path.exists("prestamos.txt"):
        print("No hay registros aún.")
        return
    
    with open("prestamos.txt", "r") as archivo:
        print(archivo.read())

def main():
    while True:
        opcion = menu()
        if opcion == "1":
            registrar_prestamo()
        elif opcion == "2":
            ver_prestamos()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()