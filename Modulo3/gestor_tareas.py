import json
import os

ARCHIVO_TAREAS = "mis_tareas.json"

def cargar_tareas():
    """Carga las tareas desde un archivo JSON. Si no existe, retorna una lista vacía."""
    if not os.path.exists(ARCHIVO_TAREAS):
        return []
    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (json.JSONDecodeError, IOError):
        return []

def guardar_tareas(tareas):
    """Guarda la lista de tareas en el archivo JSON."""
    try:
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
            json.dump(tareas, archivo, indent=4)
    except IOError:
        print("\n Error al guardar las tareas.")

def agregar_tarea(tareas):
    """Solicita una descripción y agrega una nueva tarea pendiente."""
    descripcion = input("\n Escribe la descripción de la tarea: ").strip()
    if descripcion:
        nueva_tarea = {
            "descripcion": descripcion,
            "completada": False
        }
        tareas.append(nueva_tarea)
        guardar_tareas(tareas)
        print(" Tarea agregada correctamente.")
    else:
        print(" La descripción no puede estar vacía.")

def ver_tareas(tareas):
    """Muestra todas las tareas con su índice y estado."""
    print("\n---  Lista de Tareas ---")
    if not tareas:
        print("No tienes tareas pendientes. ¡Buen trabajo!")
        return

    for i, tarea in enumerate(tareas, start=1):
        estado = "[x]" if tarea["completada"] else "[ ]"
        print(f"{i}. {estado} {tarea['descripcion']}")

def marcar_completada(tareas):
    """Cambia el estado de una tarea a completada."""
    ver_tareas(tareas)
    if not tareas:
        return

    try:
        indice = int(input("\nNúmero de tarea a completar: ")) - 1
        if 0 <= indice < len(tareas):
            tareas[indice]["completada"] = True
            guardar_tareas(tareas)
            print(" Tarea marcada como completada.")
        else:
            print(" Número de tarea inválido.")
    except ValueError:
        print(" Por favor, ingresa un número válido.")

def eliminar_tarea(tareas):
    """Elimina una tarea de la lista."""
    ver_tareas(tareas)
    if not tareas:
        return

    try:
        indice = int(input("\nNúmero de tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            eliminada = tareas.pop(indice)
            guardar_tareas(tareas)
            print(f"Tarea '{eliminada['descripcion']}' eliminada.")
        else:
            print(" Número de tarea inválido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def mostrar_menu():
    """Imprime las opciones del menú."""
    print("\n" + "="*25)
    print("   GESTOR DE TAREAS   ")
    print("="*25)
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    """Función principal que controla el flujo del programa."""
    tareas = cargar_tareas()
    
    while True:
        mostrar_menu()
        opcion = input("\n Elige una opción: ")

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            marcar_completada(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("\n ¡Hasta luego! Tus tareas están guardadas.")
            break
        else:
            print("\n Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()