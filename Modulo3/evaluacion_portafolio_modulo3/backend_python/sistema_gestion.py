import os
import time

# --- DATOS INICIALES ---
# Aca guardo los cursos y sus precios en un diccionario (clave: valor)
cursos_disponibles = {
    "Ecommerce": 150000,
    "Growth Marketing": 120000,
    "Ads Avanzado": 90000
}

# Lista vacia para ir guardando a los alumnos que vaya registrando
alumnos_inscritos = []

# --- FUNCIONES DE AYUDA ---

def limpiar_pantalla():
    # Funcion simple para borrar la consola y que se vea ordenado
    if os.name == 'nt':
        os.system('cls') # para windows
    else:
        os.system('clear') # para mac/linux

def mostrar_menu():
    # Muestro las opciones del menu principal
    print("\n--- GROWTH ACADEMY: SISTEMA INTERNO ---")
    print("1. Registrar nuevo alumno")
    print("2. Listar cursos disponibles")
    print("3. Calcular cotización (con descuentos)")
    print("4. Verificar aprobación de alumno")
    print("5. Salir")

# --- LOGICA DEL SISTEMA ---

def registrar_alumno():
    print("\n--- REGISTRO DE ALUMNO ---")
    # Pido los datos basicos por teclado
    nombre = input("Ingrese nombre del alumno: ")
    apellido = input("Ingrese apellido del alumno: ")
    
    # Valido que la edad sea un numero para que no se caiga el programa
    try:
        edad = int(input("Ingrese edad: "))
    except ValueError:
        print(">> Ojo: La edad tiene que ser un numero.")
        return

    # Pregunto si tiene beca (si escribe "si", esto queda True)
    es_becado = input("¿Tiene beca? (si/no): ").lower() == "si"

    # Guardo al alumno en un diccionario temporal
    nuevo_alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "becado": es_becado,
        "promedio": 0.0 
    }
    
    # Agrego el diccionario a la lista general
    alumnos_inscritos.append(nuevo_alumno)
    print(f">> Listo! Alumno {nombre} guardado.")

def listar_cursos():
    print("\n--- CATÁLOGO DE CURSOS ---")
    # Uso un for para recorrer el diccionario y mostrar todo
    for curso, precio in cursos_disponibles.items():
        print(f"Curso: {curso} | 💰 Precio: ${precio}")

def calcular_cotizacion():
    print("\n--- COTIZADOR ---")
    listar_cursos() # Muestro los cursos primero para que sepa cual elegir
    seleccion = input("Escribe el nombre del curso tal cual sale arriba: ")

    # Reviso si el curso que escribio existe en mi diccionario
    if seleccion in cursos_disponibles:
        precio_base = cursos_disponibles[seleccion]
        
        descuento = 0
        # Pido la edad de nuevo para ver si aplica descuento
        edad = int(input("Confirma tu edad para ver descuentos: "))

        # Aca uso if/elif para ver cuanto descuento le toca
        if edad < 18:
            print(">> Tienes descuento Joven (10%)")
            descuento = precio_base * 0.10
        elif edad > 60:
            print(">> Tienes descuento Senior (20%)")
            descuento = precio_base * 0.20
        else:
            print(">> Precio normal (sin descuento).")
        
        # Calculo final
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
    # Intento pedir las 3 notas y convertirlas a decimales
    try:
        nota1 = float(input("Nota modulo 1: "))
        nota2 = float(input("Nota modulo 2: "))
        nota3 = float(input("Nota modulo 3: "))
    except ValueError:
        print(">> Error: Tienen que ser numeros (ej: 5.5)")
        return

    # Calculo el promedio simple
    promedio = (nota1 + nota2 + nota3) / 3
    # Muestro solo 1 decimal para que se vea bien
    print(f"Promedio final: {promedio:.1f}")

    # Si es mayor o igual a 4.0 pasa, si no reprueba
    if promedio >= 4.0:
        print(">> APROBADO")
    else:
        print(">> REPROBADO")

# --- BLOQUE PRINCIPAL ---

def main():
    # Uso un while True para que el menu no se cierre hasta que yo quiera
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            registrar_alumno()
        elif opcion == "2":
            listar_cursos()
        elif opcion == "3":
            calcular_cotizacion()
        elif opcion == "4":
            verificar_aprobacion()
        elif opcion == "5":
            print("Cerrando... Nos vemos!")
            break # Rompo el ciclo para salir
        else:
            print(">> Esa opcion no vale, intenta de nuevo.")
        
        # Pausa para que alcance a leer antes de borrar pantalla
        input("\nPresiona ENTER para seguir...")
        limpiar_pantalla()

# Esto hace que el codigo arranque solo si ejecuto este archivo
if __name__ == "__main__":
    main()