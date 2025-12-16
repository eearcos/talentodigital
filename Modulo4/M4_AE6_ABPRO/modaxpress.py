import os
import shutil

INVENTARIO = "inventario.txt"
BACKUP = "inventario_backup.txt"


def leer_inventario():
    try:
        with open(INVENTARIO, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            print("\n=== INVENTARIO COMPLETO ===")
            print(contenido if contenido else "El inventario está vacío.")
    except FileNotFoundError:
        print("El archivo de inventario no existe.")


def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = input("Precio (ej: 15 USD): ")
    cantidad = input("Cantidad disponible: ")
    talla = input("Talla: ")

    nuevo_producto = f"{nombre}, {precio}, {cantidad} unidades, {talla}\n"

    try:
        with open(INVENTARIO, "a", encoding="utf-8") as archivo:
            archivo.write(nuevo_producto)
        print("Producto agregado correctamente.")
    except Exception as e:
        print("Error al agregar producto:", e)


def buscar_producto():
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").lower()

    try:
        with open(INVENTARIO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if nombre_buscar in linea.lower():
                    print("Producto encontrado:")
                    print(linea.strip())
                    return
        print("El producto no existe en el inventario.")
    except FileNotFoundError:
        print("Archivo de inventario no encontrado.")


def modificar_producto():
    nombre_modificar = input("Producto que desea modificar: ").lower()

    try:
        with open(INVENTARIO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        modificado = False
        with open(INVENTARIO, "w", encoding="utf-8") as archivo:
            for linea in lineas:
                if nombre_modificar in linea.lower():
                    print("Producto encontrado: ", linea.strip())
                    nuevo_nombre = input("Nuevo nombre del producto: ")
                    precio = input("Nuevo precio: ")
                    cantidad = input("Nueva cantidad: ")
                    talla = input("Nueva talla: ")

                    linea_modificada = f"{nuevo_nombre}, {precio}, {cantidad} unidades, {talla}\n"
                    archivo.write(linea_modificada)

                    print("Producto modificado con éxito.")
                    modificado = True
                else:
                    archivo.write(linea)

        if not modificado:
            print("El producto no se encontró en el inventario.")

    except FileNotFoundError:
        print("El archivo de inventario no existe.")


def eliminar_producto():
    nombre_eliminar = input("Producto que desea eliminar: ").lower()

    try:
        with open(INVENTARIO, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        eliminado = False
        with open(INVENTARIO, "w", encoding="utf-8") as archivo:
            for linea in lineas:
                if nombre_eliminar not in linea.lower():
                    archivo.write(linea)
                else:
                    eliminado = True

        print("Producto eliminado." if eliminado else "Producto no encontrado.")

    except FileNotFoundError:
        print("Archivo de inventario no encontrado.")


def crear_backup():
    try:
        shutil.copy(INVENTARIO, BACKUP)
        print("Backup creado exitosamente.")
    except FileNotFoundError:
        print("No hay inventario para respaldar.")
    except Exception as e:
        print("Error al crear backup:", e)


def ver_atributos():
    try:
        tamaño = os.path.getsize(INVENTARIO)
        fecha = os.path.getmtime(INVENTARIO)

        print("\n=== ATRIBUTOS DEL ARCHIVO ===")
        print(f"Tamaño: {tamaño} bytes")
        print(f"Última modificación (timestamp): {fecha}")

    except FileNotFoundError:
        print("El archivo inventario.txt no existe.")


def menu():
    while True:
        print("\n===== SISTEMA DE INVENTARIO - MODA XPRESS =====")
        print("1. Leer inventario completo")
        print("2. Agregar producto")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Crear backup")
        print("7. Ver atributos del archivo")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            leer_inventario()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            modificar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            crear_backup()
        elif opcion == "7":
            ver_atributos()
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

menu()
