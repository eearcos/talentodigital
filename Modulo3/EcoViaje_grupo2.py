# EcoViaje - Grupo 2
# Programa para gestionar reservas de excursiones
excursiones = [ 
            {"opcion":1, "nombre": "Parque Nacional Llanos de Challe", "cupo": 10, "reservas": []},
            {"opcion":2, "nombre": "Parque Nacional Fray Jorge", "cupo": 5, "reservas": []},
            {"opcion":3, "nombre": "Parque Nacional Pan de Azúcar", "cupo": 2, "reservas": [] }
]
reservas = []
print("Bienvenido a EcoViaje - Estas son nuestras excursiones disponibles:")
for excursion in excursiones:
    print(f"Opción {excursion['opcion']}: {excursion['nombre']}")
    print(f"Cupo disponible: {excursion['cupo']}")
while True:
    entrada = input("Elija excursión o 'salir' para terminar: ")
    if entrada.lower() == "salir":
        print("Programa finalizado.")
        break
    if entrada.isdigit():
        opcion = int(entrada)
        if 1 <= opcion <= len(excursiones):
            excursion_seleccionada = excursiones[opcion - 1]
            if excursion_seleccionada["cupo"] > 0:
                nombre_reserva = input("Ingrese su nombre para la reserva: ")
                excursion_seleccionada["reservas"].append(nombre_reserva)
                excursion_seleccionada["cupo"] -= 1
                print(f"Reserva exitosa para {nombre_reserva} en {excursion_seleccionada['nombre']}.")
            else:
                print(f"No hay cupo disponible en {excursion_seleccionada['nombre']}.")
        else:
            print("Opción no válida. Por favor, elija una opción válida.")


"""
TIP1: USAR
while True:
    entrada = input("Elija excursión o 'salir' para terminar: ")
    if entrada.lower() == "salir":
        print("Programa finalizado.")
        break
TIP2:
excursiones = [
    {"nombre": "Parque Nacional Villarrica", "cupo": 2, "reservas": []},
    {"nombre": "Parque Nacional Conguillio", "cupo": 2, "reservas": []}
]
"""