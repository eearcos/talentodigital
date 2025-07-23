citas = []
historial = {}
horarios_posibles = ["10:00", "11:00", "12:00", "13:00"]

def registrar_cita(nombre_mascota, fecha_cita, horario_cita, tutor_cita, tratamiento):

    cita = {
        "nombre_mascota": nombre_mascota,
        "fecha": fecha_cita,
        "horario": horario_cita,
        "tutor": tutor_cita,
        "tratamiento": tratamiento
    }
    
    citas.append(cita)
    historial[nombre_mascota].append(cita)
    print(f"Cita registrada para {nombre_mascota} el {fecha_cita} a las {horario_cita}.")
#bucle infinito ya que tengo un true y siempre se van a cumplir las condiciones en el ejemplo inicial de este caso
while True:
    print("\n--- VetCare ---")
    print("1. Registrar nueva cita")
    print("2. Ver horarios disponibles")
    print("3. Mostrar historial de mascota")
    print("4. Salir\n")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        nombre_mascota = input("Ingrese el nombre de la mascota: ")
        if nombre_mascota not in historial:
            historial[nombre_mascota] = []

        fecha_cita = input("Ingrese la fecha de la cita (DD/MM/AAAA): ")
        horario_cita = input("Ingrese la hora de la cita (HH:MM): ")

        if horario_cita not in horarios_posibles:
            print("Hora no disponible. Por favor, elija una hora válida.")
            continue

        tratamiento = input("Ingrese el tratamiento a realizar: ")
        tutor_cita = input("Ingrese el nombre del tutor: ")
        registrar_cita(nombre_mascota, fecha_cita, horario_cita, tutor_cita, tratamiento)

    elif opcion == "2":
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        print("Salieno del programa, adiós")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
