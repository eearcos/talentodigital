import os
import time

# --- DATOS INICIALES ---
cursos_disponibles = {
    "Ecommerce": 150000,
    "Growth Marketing": 120000,
    "Ads Avanzado": 90000
}

alumnos_inscritos = []

# --- FUNCIONES DE AYUDA ---

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def mostrar_menu():
    print("\n--- GROWTH ACADEMY: SISTEMA INTERNO ---")
    print("1. Registrar nuevo alumno")
    print("2. Ver alumnos inscritos")   # <--- NUEVA OPCIÓN
    print("3. Listar cursos disponibles")
    print("4. Calcular cotización (con descuentos)")
    print("5. Verificar aprobación de alumno")
    print("6. Salir")

# --- LOGICA DEL SISTEMA ---

def registrar_alumno():
    print("\n--- REGISTRO DE ALUMNO ---")
    nombre = input("Ingrese nombre del alumno: ")
    apellido = input("Ingrese apellido del alumno: ")
    
    try:
        edad = int(input("Ingrese edad: "))
    except ValueError:
        print(">> Ojo: La edad tiene que ser un numero.")
        return

    es_becado = input("¿Tiene beca? (si/no): ").lower() == "si"

    nuevo_alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "becado": es_becado,
        "promedio": 0.0 
    }
    
    alumnos_inscritos.append(nuevo_alumno)
    print(f">> Listo! Alumno {nombre} guardado.")

def ver_alumnos():   # <--- NUEVA FUNCIÓN
    print("\n--- LISTA DE ALUMNOS ---")
    if len(alumnos_inscritos) == 0:
        print(">> No hay alumnos registrados todavía.")
    else:
        for i, alumno in enumerate(alumnos_inscritos, 1):
            estado_beca = "SI" if alumno["becado"] else "NO"
            print(f"{i}. {alumno['nombre']} {alumno['apellido']} | Edad: {alumno['edad']} | Beca: {estado_beca}")

def listar_cursos():
    print("\n--- CATÁLOGO DE CURSOS ---")
    for curso, precio in cursos_disponibles.items():
        print(f"Curso: {curso} | 💰 Precio: ${precio}")

def calcular_cotizacion():
    print("\n--- COTIZADOR ---")
    listar_cursos()
    seleccion_input = input("Escribe el nombre del curso: ").lower()
    
    curso_encontrado = None
    for curso_real in cursos_disponibles:
        if curso_real.lower() == seleccion_input:
            curso_encontrado = curso_real
            break
            
    if curso_encontrado:
        precio_base = cursos_disponibles[curso_encontrado]
        descuento = 0
        edad = int(input("Confirma tu edad para ver descuentos: "))

        if edad < 18:
            print(">> Tienes descuento Joven (10%)")
            descuento = precio_base * 0.10
        elif edad > 60:
            print(">> Tienes descuento Senior (20%)")
            descuento = precio_base * 0.20
        else:
            print(">> Precio normal (sin descuento).")
        
        precio_final = precio_base - descuento
        print(f"--------------------------------")
        print(f"Precio Original: ${precio_base}")
        print(f"Descuento:      -${descuento}")
        print(f"TOTAL:          ${precio_final}")
        print(f"--------------------------------")
    else:
        print(">> Error: Escribiste mal el curso o no existe.")

def verificar_aprobacion():
    print("\n--- VERIFICADOR DE NOTAS ---")
    try:
        nota1 = float(input("Nota modulo 1: "))
        nota2 = float(input("Nota modulo 2: "))
        nota3 = float(input("Nota modulo 3: "))
    except ValueError:
        print(">> Error: Tienen que ser numeros (ej: 5.5)")
        return

    promedio = (nota1 + nota2 + nota3) / 3
    print(f"Promedio final: {promedio:.1f}")

    if promedio >= 4.0:
        print(">> APROBADO")
    else:
        print(">> REPROBADO")

# --- BLOQUE PRINCIPAL ---

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            registrar_alumno()
        elif opcion == "2":         # <--- NUEVA LÓGICA
            ver_alumnos()
        elif opcion == "3":
            listar_cursos()
        elif opcion == "4":
            calcular_cotizacion()
        elif opcion == "5":
            verificar_aprobacion()
        elif opcion == "6":         # <--- SALIR ES AHORA EL 6
            print("Cerrando... Nos vemos!")
            break
        else:
            print(">> Esa opcion no vale, intenta de nuevo.")
        
        input("\nPresiona ENTER para seguir...")
        limpiar_pantalla()

if __name__ == "__main__":
    main()